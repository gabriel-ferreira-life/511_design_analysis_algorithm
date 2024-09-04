def binary_search(list, target):

    """
    Returns the index position of the target if found, else returns None
    """
        
    first = 0
    last = len(list) - 1

    while first <= last:
        midpoint = (first + last) // 2

        if list[midpoint] == target:
            return midpoint
        elif list[midpoint] < target:
            first = midpoint + 1
        else:
            last = midpoint - 1

    return None 

def verify(index):
    if index is not None:
        print("Target found at index: ", index)
    else:
        print("Target not found in the list.")


numbers = [3, 4, 5, 7, 11, 12] # required to be sorted
result = binary_search(numbers, 6)
verify(result)

