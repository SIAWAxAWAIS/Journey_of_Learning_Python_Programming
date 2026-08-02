# doc_strings is always added right after the function and right above the function body

def square(a):
    '''Takes a number a, and returns it square root'''
    print(a**2)

square(3)
print(square.__doc__)