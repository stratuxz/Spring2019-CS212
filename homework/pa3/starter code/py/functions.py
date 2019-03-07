import csv
from graph import Graph

def process_csv(file_name):
    data = []
    with open(file_name, 'r') as some_file:
        csv_file = csv.reader(some_file, delimiter=',', quotechar='"')
        for row in csv_file:
            data.append(row)
    return data

def fileToMap(class_instance, file_name):
    # keep track of destinations
    temp = []
    file_data = process_csv(file_name)

    #only want to add unique destinations
    for data in file_data:
        if data[0] not in temp:
            temp.append(data[0])
            class_instance.add_vertex(data[0])

        if data[1] not in temp:
            temp.append(data[1])
            class_instance.add_vertex(data[1])
            
    # convert weight to int while we're at it
        data[2] = int(data[2])

        class_instance.connect_vertex(data[0], data[1], data[2], True)
    
def calculateMstTime(mst_graph):
    time = 0
    for i in mst_graph:
        time += i[0]
    return str(time) + " minutes"

# look for end key in the computed-short graph
def searchDestination(key, computed_map):
    if key in computed_map:
        return computed_map[key]

def fasterDeliveryPath(class_instance, file_name):
    delivery_list = process_csv(file_name)

    # convert to a single list (not necessary, just makes it easier to read/use)
    delivery_route = [house[0] for house in delivery_list]

    delivery_path = []

    newGraph = Graph()

    # compute dijkstra's algorithm on each delivery 
    for i in range(0, len(delivery_route)):

        short_path = class_instance.compute_shortest_path(delivery_route[i])

        if i != len(delivery_route)-1:
            time_reached = searchDestination(delivery_route[i+1], short_path)
            delivery_path.append((delivery_route[i], delivery_route[i+1], int(time_reached)))
        
        #if we have reached the last element, record shortest distance back to starting point
        else:
            time_reached = searchDestination(delivery_route[0], short_path)
            delivery_path.append((delivery_route[i], delivery_route[0], int(time_reached)))

        newGraph.add_vertex(delivery_route[i])
    
    for deliveries in delivery_path:
        newGraph.connect_vertex(deliveries[0], deliveries[1], deliveries[2], True)

    # complete mst based on first delivery 
    shorter_path = newGraph.compute_minimum_spanning_tree(deliveries[0][0])
        
    return shorter_path

def printFasterPath(faster_path):
    print("Route: ")
    for info in faster_path:
        print(info[1], '->', info[2])