## gridTraveler
# # Recursive approach
# def gridTraveler(m,n):
#     if((m==1)&(n==1)):
#         return 1
#     elif((m==0)|(n==0)):
#         return 0
#     else:
#         return gridTraveler(m-1, n) + gridTraveler(m, n-1)
    

# Memoization approach
def gridTraveler(m,n, memo={}):
    key = str(m) + "," + str(n)
    if key in memo:
        return memo[key]
    if((m==1)&(n==1)):
        return 1
    elif((m==0)|(n==0)):
        return 0
    else:
        memo[key] = gridTraveler(m-1, n, memo) + gridTraveler(m, n-1, memo)
        return memo[key]
    

print(gridTraveler(1,1))
print(gridTraveler(3,2))
print(gridTraveler(2,3))
print(gridTraveler(3,3))
print(gridTraveler(18,18))

# Example usage
memo = {}
result = gridTraveler(3, 3, memo)
print(f"Number of ways to travel a 3x3 grid: {result}")
print("Memoization dictionary:", memo)