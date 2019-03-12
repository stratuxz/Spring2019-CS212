import csv
from graph import Graph

def process_csv(file_name):
    data = []
    with open(file_name, 'r') as some_file:
        csv_file = csv.reader(some_file, delimiter=',', quotechar='"')
        for row in csv_file:
            data.append(row)
    return data

def fileToMap(graph_instance, file_name):
    # keep track of houses
    houses = []

    file_data = process_csv(file_name)

    for data in file_data:

        #only want to add unique houses
        if data[0] not in houses:
            houses.append(data[0])
            graph_instance.add_vertex(data[0])

        if data[1] not in houses:
            houses.append(data[1])
            graph_instance.add_vertex(data[1])
            
        # convert weight to int while we're at it
        data[2] = int(data[2])

        graph_instance.connect_vertex(data[0], data[1], data[2], True)

def calculateMstTime(mst_graph):
    time = 0
    for house in mst_graph:
        time += house[0]
    return str(time) + " minutes"

def shorterDeliveryPath(graph_instance, file_name):
    delivery_list = process_csv(file_name)

    # convert to a single list (not necessary, just makes it easier to read/use)
    delivery_route = [house[0] for house in delivery_list]

    # keep track of paths and weight
    short_path = {}
    newGraph = Graph()

    for house in range(0, len(delivery_route)):
        
        current_house = delivery_route[house]
        newGraph.add_vertex(current_house)

        # compute dijkstra's algorithm on each delivery 
        short_path = graph_instance.compute_shortest_path(current_house)
    
        for house in short_path:
            # if current house is not equal to itself while going through
            # the short path dictionary AND
            # if the house exists on delivery route  
            if current_house != house and house in delivery_route:
                time = short_path[house]
                newGraph.connect_vertex(current_house, house, time)
                #path.append((current_house, deliveries, time))

    # compute MST based on first delivery
    path = newGraph.compute_minimum_spanning_tree(delivery_route[0])
    return path

def printFasterPath(shorter_path):
    print("Route: ")
    size = len(shorter_path)
    for i in range(0, size):
        next = shorter_path[i][2]
        current = shorter_path[i][1]
        #if not at at element of list
        if i != size-1:
            #if next delivery isnt current delivery for next element
            if next != shorter_path[i+1][1]:
                #then flip
                print(next, '->', current)
            else:
                print(current, '->', next)
        else:
            print(current, '->', next)
