# f = open("file.txt" , 'r')
# print(type(f))

# f.seek(10)

# data = f.read(5)
# print(data)



# f = open("file.txt" , 'r')
# print(type(f))

# f.seek(10)

# print(f.tell())
# data = f.read(5)
# print(data)


with open("sample.txt" , 'w') as file:
    file.write("Life is Too Short So Live it with full Enjoyment!")
    file.truncate(17)

with open("sample.txt" , 'r') as file:
    print(file.read())