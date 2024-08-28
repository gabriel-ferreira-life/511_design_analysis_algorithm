## canSum function

# # Recursive approach
# def canSum(targetSum, numbers):
#     if(targetSum < 0):
#         return False
#     if(targetSum == 0):
#         return True

#     for num in numbers:
#         remainder = targetSum - num
#         if canSum(remainder, numbers) == True:
#             return True
        
#     return  False

# Memoization approach approach
def canSum(targetSum, numbers, memo=None):
    if memo is None:
        memo = {}
    if targetSum in memo:
        return memo[targetSum]
    if(targetSum == 0):
        return True
    if(targetSum < 0):
        return False
    

    for num in numbers:
        remainder = targetSum - num
        
        if canSum(remainder, numbers, memo) == True:
            memo[targetSum] = True
            return True
    
    memo[targetSum] = False
    return  False
        
    
## Results
print(canSum(7, [2, 3])) ## True
print(canSum(7, [5, 3, 4, 7])) ## True
print(canSum(7, [2, 4])) ## False
print(canSum(8, [2, 3, 5])) ## True 