import csv
from functions import *
from graph import Graph

print("*** Tier 1 Route Planner***")

print("Enter map file: ")
#first_map = input()
housemap = Graph()
fileToMap(housemap, "map1.txt")

print("Enter destination file: ")
#first_dest = input()
show = process_csv("deliveries1.txt")
first_mst  = housemap.compute_minimum_spanning_tree('A')

print("Total Transit Time:")
print(calculateMstTime(first_mst))


print("*** Tier 2 Route Planner***")
print("Enter map file: ")
#second_map = input()
routes = Graph()
fileToMap(routes, "map2.txt")

print("Enter destination file: ")
#second_dest = input()
second_mst = fasterDeliveryPath(routes, "deliveries2.txt")

print("Total Transit Time:")
print(calculateMstTime(second_mst))

print("*** Tier 3 Route Planner***")
print("Enter map file: ")
#third_map = input()
deliveryMap = Graph()
fileToMap(deliveryMap, "map3.txt")

print("Enter destination file: ")
#third_dest = input()
third_mst = fasterDeliveryPath(deliveryMap, "deliveries3.1.txt")

print("Total Transit Time: ")
print(calculateMstTime(third_mst))
printFasterPath(third_mst)