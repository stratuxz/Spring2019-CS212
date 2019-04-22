import sqlite3

def createDB():
    word_conn = sqlite3.connect("wordDictionary.db") #open connection
    word_cursor = word_conn.cursor()
    word_cursor.execute("DROP TABLE Dictionary")
    word_cursor.execute("""CREATE TABLE IF NOT EXISTS Dictionary (
                               word TEXT UNIQUE);""")

    word_conn.commit()

    with open("words.txt", "rt") as word_file:

        for word in word_file:
            word = word.strip()
            word_cursor.execute("INSERT OR IGNORE INTO Dictionary(word) VALUES(?)", [word])
            word_conn.commit()

    word_conn.close()