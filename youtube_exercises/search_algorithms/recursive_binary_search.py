def recursive_binary_search(list, target):
    """
    Returns True if found, else returns False
    """

    if len(list) == 0:
        return False
    
    midpoint = len(list)//2

    if list[midpoint] == target:
        return True
    elif list[midpoint] < target:
        return recursive_binary_search(list[midpoint+1:], target)
    else:
        return recursive_binary_search(list[:midpoint], target)

    

def verify(result):
        print("The result is: ", result)


numbers = [3, 4, 5, 7, 11, 12] # required to be sorted
result = recursive_binary_search(numbers, 3)
verify(result)

