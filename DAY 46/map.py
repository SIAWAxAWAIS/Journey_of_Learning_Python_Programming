def cube(x):
    return x*x*x

print(cube(4))

List = [6,3,2,4,8,9,3]
# newlist = []
# for item in List:
#     newlist.append(cube(item))

newlist = list(map(cube , List))
print(newlist)