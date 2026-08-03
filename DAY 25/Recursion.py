# factorial(0) = 1
# factorial(1) = 1
# factorial(2) = 2*1
# factorial(3) = 3*2*1 and so on


# def factorial(n):
#     if(n==0 or n==1):
#         return 1
#     else:
#         return n * (factorial(n-1))

# print(factorial(5))
# print(factorial(6))
# print(factorial(7))


# fabonacci series

def fabonacci(n):
    if(n==0):
        return 0
    elif(n==1):
        return 1
    else:
        return  fabonacci(n-1) + fabonacci(n-2)

print(fabonacci(7))
print(fabonacci(6))