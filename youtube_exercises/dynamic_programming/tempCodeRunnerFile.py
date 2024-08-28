# Recursive approach
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