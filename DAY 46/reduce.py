from functools import reduce
l = [6,4,5,2]

sum = reduce(lambda a , b: a+b , l)
print(sum)