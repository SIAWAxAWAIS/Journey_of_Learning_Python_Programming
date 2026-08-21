# def square(x):
#     return x *4

def apply(fx , value):
    return 8 + fx(value)

# alternative Lambda


square = lambda x: x*4
cube = lambda y: y*y*y
avg = lambda a ,b: (a+b) / 2
print(square(4))
print(cube(5))
print(avg(10,6))
print(apply (lambda y: y*y*y ,2))