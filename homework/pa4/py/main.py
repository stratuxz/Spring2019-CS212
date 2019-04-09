#for CSV parsing
import csv
from math import log2

class TreeNode:
   def __init__(self):
      self.children = {}
      self.value = ""

def process_csv(file_name):
   data = []
   with open(file_name, 'r') as some_file:
      csv_file = csv.reader(some_file, delimiter=',' or '|', quotechar='"')
      for row in csv_file:
         data.append(row)
   return data

def calculate_entropy(outcome_levels):
   denominator = 0.0
   for key in outcome_levels:
      denominator += outcome_levels[key]
   
   entropy = 0.0
   for key in outcome_levels:
      ratio = outcome_levels[key] / denominator
      logged = log2(ratio)
      entropy += -ratio * logged
   return entropy

def build_frequency_distribution(sequence):
   distribution = {}
   for item in sequence:
      if not item in distribution:
         distribution[item] = 0
      distribution[item] += 1
   return distribution

def get_observations(matrix, column):
   result = []
   for i in range(len(matrix)):
      result.append(matrix[i][column])
   return result

def reduce_matrix(matrix, column, predictor):
   result = []
   for i in range(len(matrix)):
      if matrix[i][column] == predictor:
         result.append(matrix[i])
   return result

def find_max_gain(matrix, outcome_column, entropy):
   if len(matrix) == 0:
      return -1
   
   information_gain = []
   for column in range(len(matrix[0])):
      if column == outcome_column:
         information_gain.append(-1)
         continue
      observations = get_observations(matrix, column)
      observation_levels = build_frequency_distribution(observations)
      local_entropy = 0.0
      for level in observation_levels:
         reduced_matrix = reduce_matrix(matrix, column, level)
         reduced_observations = get_observations(reduced_matrix, outcome_column)
         local_entropy += observation_levels[level] / len(observations) * calculate_entropy(build_frequency_distribution(reduced_observations))
      information_gain.append(entropy - local_entropy)
   
   most_gain = 0
   for i in range(1, len(information_gain)):
      if information_gain[i] > information_gain[most_gain]:
         most_gain = i
   return most_gain

def build_tree(matrix, predictors, outcome_column):
   observations = get_observations(matrix, outcome_column)
   entropy = calculate_entropy(build_frequency_distribution(observations))
   if(entropy < 0.01):
      node = TreeNode()
      node.value = matrix[0][outcome_column]
      return node
   
   col = find_max_gain(matrix, outcome_column, entropy)
   node = TreeNode()
   node.value = predictors[col]

   selected_observations = get_observations(matrix, col)
   selected_levels = build_frequency_distribution(selected_observations)
   for level in selected_levels:
      reduced_matrix = reduce_matrix(matrix, col, level)
      node.children[level] = build_tree(reduced_matrix, predictors, outcome_column)
   return node
#--------------------------------------------------------------------------------------
def buildTreeFromFile():
   file_name = input("Enter a .csv file: ")
   file_result = process_csv(file_name)
   # outcome change to input row name
   user_outcome = input("Enter a outcome variable: ")
   predictor_variables = file_result[0]
   file_result = file_result[1:]
   tree = build_tree(file_result, predictor_variables, int(user_outcome))
   
   return tree

def treeToVector(decision_tree, depths = []):

   node = decision_tree.value
   num_children = len(decision_tree.children)
   # at root
   if len(depths) == 0:
      edge = "NULL"
      depths.append([edge, node, num_children])

   for key, tree_node in decision_tree.children.items():
      edge = key
      node = tree_node.value
      num_children = len(tree_node.children)

      depths.append([edge, node, num_children])

   for tree_node in decision_tree.children.values():
      treeToVector(tree_node, depths)
   
   return depths

def transferToFile(tree_vector):
   file_name = input("Create a .txt file: ")

   with open(file_name, 'w') as tree_file:
      for node in tree_vector:
         tree_file.write("{0}|{1}|{2}\n".format(*node))

def fileToVector():
   file_name = input("Enter a tree file: ")
   tree_nodes = process_csv(file_name)

   return tree_nodes


def createTree(tree_vector):

   if tree_vector[0][0] == "NULL":
      node = TreeNode()
      node.value[0][1]
      num_children = int(tree_vector[0][2])

   for tree_nodes in tree_vector:
      num_children = int(tree_nodes[2])
      node.value = tree_nodes[1]
      start = tree_vector.index(tree_nodes)
      
      if num_children > 0:

         for i in range(start+1, num_children+1):

            node.children[tree_nodes[0]] = tree_vector[i][0]
            # start = num_children
            num_children += int(tree_nodes[i][2])

   pass 

   return node



def PredcitedFile():
   file_name = input("Enter a .csv file: ")
   file_result = process_csv(file_name)

   # outcome change to input row name
   user_outcome = int(input("Enter a outcome variable: "))
   predictor_variables = file_result[0]
   file_result = file_result[1:]

   tree = build_tree(file_result, predictor_variables, user_outcome)

   predictor_file = input("Create a .csv file for predictors: ")

   with open(predictor_file, 'w') as predicted_file:
      for var in predictor_variables:
         predicted_file.write(var)
         new = predictOutcomes(predictor_variables, tree, file_result)
         for info in new:
            predicted_file.write(info)
   pass


def predictOutcomes(predictors, decision_tree, data):

   node = decision_tree.value

   if node in predictors:
      index = predictors.index(node)
   
   for row in data:
      if len(decision_tree.children) == 0:
         row.append(decision_tree.value)
         return data 

      for edge, tree_node in decision_tree.children.items():
         if row[index] in edge:
            predictOutcomes(predictors, tree_node, data)

   return data
   

global root

def main():

   print("1. Build tree from file\n2. Write to File\n3. Predict Outcome\n4. Read from file")
   option = int(input("Enter an option: "))
   

   while option == 1 or option == 2 or option == 3 or option == 4:
      if option == 1:
         root = buildTreeFromFile()
      elif option == 2:
         tree_list = treeToVector(root)
         transferToFile(tree_list)
      elif option == 3:
         #PredcitedFile()
         break
      elif option == 4:
         tree_matrix = fileToVector()
         break
         
      print("1. Build tree from file\n2. Write to File\n3. Predict Outcome\n4. Read from file")
      option = int(input("Enter an option: "))

   print("done") 
  
if __name__ == '__main__':
   main()
