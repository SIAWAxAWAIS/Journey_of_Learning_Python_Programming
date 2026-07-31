tup = (1,5,7,9,7,4,4,23,True)
print(type(tup) , tup)
print(tup[0])
print(tup[1])
print(tup[2])
print(tup[3])

if True in tup:
    print("True is present in tuple")
else:
    print("True is not present in the tuple")


tup1 = tup[0:5]
print(tup1)
print(tup)