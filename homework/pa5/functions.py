from collections import defaultdict
from re import findall
import sqlite3

def calculateEditDistance(first, second):
    matrix = []

    # construct matrix
    for i in range(len(first) + 1):
        matrix.append([])
        for j in range(len(second) + 1):
            matrix[i].append(0)

    # fill in first row
    for i in range(len(matrix[0])):
        matrix[0][i] = i

    # fill in first column
    for i in range(len(matrix)):
        matrix[i][0] = i

    # compute rest of matrix
    for i in range(1, len(matrix)):
        for j in range(1, len(matrix[i])):

            top_cost = matrix[i - 1][j] + 1
            left_cost = matrix[i][j - 1] + 1
            diagonal_cost = matrix[i - 1][j - 1]

            # add 1 to diagonal if chars don't match
            if(first[i - 1] != second[j - 1]):
                diagonal_cost += 1

            best_choice = min(top_cost, left_cost, diagonal_cost)
            matrix[i][j] = best_choice
    return matrix[len(matrix) - 1][len(matrix[0]) - 1]
#-----------------------------------------------------------------------------#

def checkWordExists(file_word):
    connection = sqlite3.connect("wordDictionary.db")
    word_cursor = connection.cursor()

    word_cursor.execute("""SELECT word 
                           FROM Dictionary
                           WHERE word = :find""", {'find': file_word})
    # get word if file_word found in DB 
    fetched_word = word_cursor.fetchone()
    connection.close()

    if fetched_word is None:
        return False
    else:
        return True

def classifyEditDistance(word_to_correct):

    distances = defaultdict(list)
    possible_corrections = []
    # if word not found in DB, calculate edit distance
    if (checkWordExists(word_to_correct) == False):

        connection = sqlite3.connect("wordDictionary.db")
        word_cursor = connection.cursor()

        word_cursor.execute("SELECT * FROM Dictionary")
        # get all the words(rows) in the DB
        fetched_word = word_cursor.fetchall()

        for word in fetched_word:
            word = word[0]
            edit = calculateEditDistance(word_to_correct, word)
            distances[edit].append(word)

        size = len(possible_corrections)
        #smallest to largest (edit distance)
        for k, values in sorted(distances.items()):
            for v in values:
                if size < 10: #fill until len is 10
                    possible_corrections.append((v,k))
                    size = len(possible_corrections)
                else:
                    return possible_corrections
  
    return possible_corrections
 
def inputFile(input_file_name):
    content = []

    with open(input_file_name, 'r') as fix_file:
        for line in fix_file:
            #separate special chars from word 
            content += findall(r"[\w']+|[.,!?;\n\t]", line)

    for word in content:
        index = content.index(word)

        if word not in ['.', ',', '?', '!', ';', '\n', '\t']: #check for punctuations
            corrections = classifyEditDistance(word)
            size = len(corrections)
        else:
            size = 0

        if size > 0:
            print("\nUnknown Word: {0}".format(word), end='\n')
            print("1. None are correct.")
            for count, possible_words in enumerate(corrections, start=2):
                print("{0}. {1}".format(count, possible_words[0]), end='\n')

            choice = int(input("Enter a selection: "))
    
            connection = sqlite3.connect("wordDictionary.db")
            word_cursor = connection.cursor()

            while choice > 11 or choice == 0:
                choice = int(input("Enter a selection: "))

            if choice == 1:
                insert_word = input("Enter correct word: ")
                word_cursor.execute("INSERT OR IGNORE INTO Dictionary(word) VALUES(:new_word)", {'new_word': insert_word})
                connection.commit() 

                content[index] = insert_word  #replace word with correct version
                dataFiles(corrections, word, insert_word)

            elif choice in range(2,12):
                word_index = choice-2
                content[index] = corrections[word_index][0] #replace word with correct version
                dataFiles(corrections, word, None, word_index)

            connection.close()
    return content

def destinationFile(destination_file, content):
    exceptions = ['.', ',', '?', '!', ';', '\n', '\t']
    with open(destination_file, 'w') as fixed_file:
        for data in range(len(content)-1):
            if content[data+1] in exceptions or content[data] in exceptions:
                fixed_file.write("{0}".format(content[data])) #dont add space
            else:
                fixed_file.write("{0} ".format(content[data])) #add space
        
        fixed_file.write(content[len(content)-1]) #space doesn't matter for last

def dataFiles(corrections, word, input_word=None, position = None):
    with open("{0}.dat".format(word), 'w') as dat:
        if input_word != None:
            dat.write("{0} 0\n".format(input_word))
        
        if position != None:
            first = corrections.pop(position)
            dat.write("{0} {1}\n".format(*first))
        
        for words in corrections:
            dat.write("{0} {1}\n".format(*words))

    corrections.clear() #clear data