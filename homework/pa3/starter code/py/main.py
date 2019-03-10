import csv
from functions import *
from graph import Graph

print("*** Tier 1 Route Planner***")
print("Enter map file: ")
#first_map = input()
firstCityMap = Graph()
fileToMap(firstCityMap, "map2.txt")

print("Enter destination file: ")
#first_dest = input()
show = process_csv("deliveries2.txt")
first_mst  = firstCityMap.compute_minimum_spanning_tree(show[0][0])

print("Total Transit Time:")
print(calculateMstTime(first_mst))

print("*** Tier 2 Route Planner ***")
print("Enter map file: ")
#second_map = input()
secondCityMap = Graph()
fileToMap(secondCityMap, "map2.txt")

print("Enter destination file: ")
#second_dest = input()
second_mst = fasterDeliveryPath(secondCityMap, "deliveries2.txt")
print("Total Transit Time:")
print(calculateMstTime(second_mst))

print("*** Tier 3 Route Planner ***")
print("Enter map file: ")
#third_map = input()
thirsCityMap = Graph()
fileToMap(thirsCityMap, "map2.txt")

print("Enter destination file: ")
#third_dest = input()
third_mst = fasterDeliveryPath(thirsCityMap, "deliveries2.txt")

print("Total Transit Time: ")
print(calculateMstTime(third_mst))
printFasterPath(third_mst)