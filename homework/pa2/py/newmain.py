import csv 
from graph import Graph
from locations import Locations

def process_csv(file_name):
    data = []
    with open(file_name, 'r') as some_file:
        csv_file = csv.reader(some_file, delimiter=',', quotechar='"')
        for row in csv_file:
            data.append(row)
    return data

def dataToMap(data_list):
    for elements in data_list:
        elem = elements
        hsuMap.connect_vertex(*elem)

hsuMap = Graph()
loc = Locations()

# add nodes
for i in loc._locations:
    hsuMap.add_vertex(i)

mapData = process_csv("distances.csv")
dataToMap(mapData)

print("** HSU Transit Time Calculator **")
print("Enter starting location: ")
start = input()
beg_code = loc.look_up(start)
print("Enter destination: ")
end = input()
end_code = loc.look_up(end)
print("Etimated travel time: ")
total = input()







