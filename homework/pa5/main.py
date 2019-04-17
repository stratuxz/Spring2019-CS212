import sqlite3
import os
from collections import defaultdict

def main():
    #os.chdir('Users/blurry.soul/Documents/CS 212 - Algorithms/Spring2019-CS212/homework/pa5')

    auto_correct = sqlite3.connect('Words.db')
    cursor = auto_correct.cursor()
    drop_table = "DROP TABLE WordDictionary"
   # cursor.execute(drop_table)
    create_table = "CREATE TABLE WordDictionary(words text)"
    cursor.execute(create_table)

    
    with open("words.txt", 'r', ) as word_file:
        for word.strip in word_file:
            word = word.strip()
            insert_table = "INSERT INTO WordDictionary values({0});".format(word)
            cursor.execute(insert_table)


    

    
            
    
    
    cursor.close()
    auto_correct.close()

    pass
    #os.close()




def calculateEditDistance(first, second):
    matrix = []

    # construct matrix
    for i in range(len(first)+1):
        matrix.append([])
        for j in range(len(second)+1):
            matrix[i].append(0)

    # fill in first row
    for i in range(len(matrix[0])):
        matrix[0][i] = i

    # fill in first column
    for i in range(len(matrix)):
        matrix[i][0] = i

    # compute rest of matrix
    for i in range(len(matrix)):
        for j in range(len(matrix[i])):

            top_cost = matrix[i - 1][j] + 1
            left_cost = matrix[i][j - 1] + 1
            diagonal_cost = matrix[i - 1][j - 1]

            # add 1 to diagonal if chars don't match
            if(first[i - 1] != second[j - 1]):
                diagonal_cost += 1

            best_choice = min(top_cost, left_cost, diagonal_cost)
            matrix[i][j] = best_choice
            
    return matrix[len(matrix) - 1][len(matrix[0]) - 1]


def classifyEditDistance(auto_correct):
    distances = defaultdict(list)

    with open("words.txt", 'r') as word_file:
        
        for word in word_file:

            word = word.strip()

            if auto_correct != word:
                edit_count = calculateEditDistance(auto_correct, word)
                distances[edit_count].append(word)

    possible_corrections = []

    size = len(possible_corrections)

    while size < 11:

        for key, values in sorted(distances.items()):

            for word in values:

                possible_corrections.append(word)

                size = possible_corrections



            #possible_corrections = [value for key, values in sorted(distances.items()]
            #possible_corrections = [word for key, values in sorted(distances.items()) for word in values]

                
        #print(possible_corrections)

    return possible_corrections


if __name__ == "__main__":
    print(calculateEditDistance("dog", "of"))

    #classifyEditDistance("raccoon")


# os.close()
# auto_correct.close() 

    

