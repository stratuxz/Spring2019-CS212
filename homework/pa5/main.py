def calculate(first, second, first_index, second_index, mem = []):
    cost = 0
     
    if first_index >= len(first):
        return len(second) - second_index

    elif second_index >= len(second):
        return len(first) - first_index
    
    if first[first_index] == second[second_index]:
        return calculateEditDistance(
        first, 
        second,
        first_index + 1, 
        second_index + 1,
        mem)
    
    

