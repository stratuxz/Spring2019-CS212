# Zahory Velazquez
# id: 012896205
# PA 2 - program that has user input an HSU location and prints the shortest time
#        and shortest path

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

def secondsToMin(time_seconds):
    #show 2 decimal places
    print("{:.2f}".format(time_seconds/60) + " minutes")

# look for end key in the computed-short graph
def searchShortest(key, computed_map):
    if key in computed_map:
        return computed_map[key]


mapData = process_csv("distances.csv")
hsuMap = Graph()
location = Locations()    

for i in location._locations:
    hsuMap.add_vertex(i)

for items in mapData:
    # change last element in list to a float (for adding purposes)
    items[2] = float(items[2])

    # each element in list becomes an argument for paramter
    hsuMap.connect_vertex(*items)

print("** HSU Transit Time Calculator **")

print("TIER 1")
print("Enter starting location: ")
start = input()
beg_code = location.look_up(start)
paths = hsuMap.compute_shortest_path(beg_code)


print("Enter destination: ")
end = input()
end_code = location.look_up(end)

print("Etimated travel time: ")
time = searchShortest(end_code, paths)
secondsToMin(time[0])

print("Tier 2")
print("Enter starting location: ")
begin = input()
begin_key = location.look_up(begin)
short_paths = hsuMap.compute_shortest_path(begin_key)

print("Enter destination: ")
destination = input()
destination_key = location.look_up(destination)

print("Etimated travel time: ")
total = searchShortest(destination_key, short_paths)
secondsToMin(total[0])

print("You will travel to: ") 
for i in total[1]:
    # each list represents the locations within the keys traveled
    print(location._locations[i])
