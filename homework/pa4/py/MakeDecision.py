from main import process_csv, TreeNode, build_tree

def buildTreeFromFile():
    file_name = input("Enter a .csv file: ")
    file = process_csv(file_name)
    user_outcome = input("Enter a outcome variable: ")
    predictor_variables = file[0]
    result = file[1:]
    tree = build_tree(result, predictor_variables, user_outcome)
    
    return tree
    
def TreeToFile(decision_tree):

    decision_tree = TreeNode()

    file_name = input("Enter a name to create a .txt ile: ")
    with open(file_name) as write_file:
        write_file.write(decision_tree)