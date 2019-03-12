#Zahory Velazquez
#03.12.2019

import csv
from functions import *
from graph import Graph

print("*** Tier 1 Route Planner***")
print("Enter map file: ",end='')
first_map = input()
firstCityMap = Graph()
fileToMap(firstCityMap, first_map)

print("Enter destination file: ", end='')
first_dest = input()
delivery_locs = process_csv(first_dest)
first_mst  = firstCityMap.compute_minimum_spanning_tree(delivery_locs[0][0])

print("Total Transit Time: ", end= "")
print(calculateMstTime(first_mst), end='\n\n')

print("*** Tier 3 Route Planner ***")
print("Enter map file: ", end='')
third_map = input()
thirsCityMap = Graph()
fileToMap(thirsCityMap, third_map)

print("Enter destination file: ", end='')
third_dest = input()
third_mst = shorterDeliveryPath(thirsCityMap, third_dest)

print("Total Transit Time: ", end='')
print(calculateMstTime(third_mst))
printFasterPath(third_mst)
