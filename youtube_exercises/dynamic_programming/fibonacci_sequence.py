"""source: https://www.youtube.com/watch?v=oBt53YbR9Kk"""

 # Recursive approach
# def fib(n):
#     if n<=2:
#         return 1
#     else:
#         return fib(n-1) + fib(n-2)
    

# Memoization approach
def fib(n, memo={}):
    if n in memo:
        return memo[n]
    if n <= 2:
        return 1
    else:
        memo[n] = fib(n-1, memo) + fib(n-2, memo)
        return memo[n]



n = 6
memo = {}
result = fib(n, memo)
print(f"The Fibonacci number for {n} is: {result}")
print("Memoization dictionary:", memo)