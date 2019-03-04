import csv
from newmain import *
from graph import Graph

print("*** Route Planner***")

print("Enter map file: ")
#first_map = input()
first_file = filefix("map1.txt")
housemap = Graph()
fileToMap(housemap, first_file)

print("Enter destination file: ")
#first_dest = input()

first_mst  = housemap.compute_minimum_spanning_tree()
calculateMstTime(fist_mst)
