import csv
from graph import Graph

def process_csv(file_name):
    data = []
    with open(file_name, 'r') as some_file:
        csv_file = csv.reader(some_file, 
                            delimiter=',', 
                            quotechar='"'
                            )
        for row in csv_file:
            data.append(row)
    return data

def filefix(file_name):
    file_data = process_csv(file_name)
    for data in file_data:
        data[2] = int(data[2])
    return file_data

def fileToMap(class_instance, file_data):
    temp = []

    for data in file_data:
        if data[0] not in temp:
            temp.append(data[0])
            class_instance.add_vertex(data[0])

        if data[1] not in temp:
            temp.append(data[1])
            class_instance.add_vertex(data[1])

        class_instance.connect_vertex(*data, True)

    temp.clear()

def calculateMstTime(mst_graph):
    sum = 0
    for i in mst_graph:
        sum += i[0]
    return sum + 'minutes'