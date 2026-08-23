List = [6,3,2,4,8,9,3]

def Filter_funtion(x):
    return x > 3

newList = list(filter(Filter_funtion , List))
print(newList)
