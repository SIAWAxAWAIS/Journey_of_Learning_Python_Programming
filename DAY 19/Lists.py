# marks = [75,59,56]
# print(marks)
# print(type(marks))
# print(marks[0]) 
# print(marks[1]) 
# print(marks[2])


# storing different type of data

# marks = [75,59,56 , "Ali Khan" ,"Char Char" , True]
# print(marks)
# print(type(marks))
# print(marks[0]) 
# print(marks[1]) 
# print(marks[2])
# print(marks[3])
# print(marks[4])
# print(marks[5])

# Negative indexing


# marks = [75,59,56 , "Ali Khan" ,"Char Char" , True]
# print(marks[-3])
# print(marks[len(marks)-3])
# print(marks[6-3])          # Positive indexing
# print(marks[3])               # Positive indexing




# marks = [75,59,56 , "Ali Khan" ,"Char Char" , True]

# if 75 in marks:
#     print("YES")
# else:
#     print("No")


# marks = [75,59,56 , "Ali Khan" ,"Char Char" , True]
# print(marks)
# print(marks[:])
# print(marks[:-1])
# print(marks[::2])  # Jump to



# Comprehension list

list = [i for i in range(5) ]
print(list)
list = [i*i for i in range(5) ]
print(list)
list = [i*i for i in range(5) if i%2==0 ]
print(list)