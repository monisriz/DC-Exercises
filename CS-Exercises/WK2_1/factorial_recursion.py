def factorial(n):
    if n <= 1:
        return n
    else:
        return  n * factorial(n - 1)

print(factorial(10))


# Loop method:

# def factorial_while(self, n):
#     result = 1
#     while(n > 0):
#         result = result * n
#         n = n - 1
#     return result
