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

hsuMap = Graph()
loc = Locations()

for i in loc._locations:
    hsuMap.add_vertex(i)

mapData = process_csv("distances.csv")

for items in mapData:
    hsuMap.connect_vertex(*items)


print("** HSU Transit Time Calculator **")
print("Enter starting location: ")
start = input()
beg_code = loc.look_up("Cedar")
hsuMap.compute_shortest_path(beg_code)
print("Enter destination: ")
#end = input()
#end_code = loc.look_up("FWH")
print("Etimated travel time: ")
#total = input()







