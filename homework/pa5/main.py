# Zahory Velazquez
# 04.21.2019
# completion time: didn't keep track

from dbdict import createDB
from functions import inputFile, destinationFile

def main():
    # rebuilds itself each time
    createDB() #  NOTE: Comment out if you want DB to save new inputs

    input_file = input("Enter a file to correct: ")
    destination_file = input("Enter a destination file: ")

    data = inputFile(input_file)

    destinationFile(destination_file, data)

if __name__ == "__main__":
    main()
