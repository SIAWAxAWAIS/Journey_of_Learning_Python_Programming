# file = open("myfile.txt" , 'r')
# # print(file)

# text = file.read()
# print(text)
# file.close()


# file1 = open('myfile1.txt' , 'w')

# text1 = file1.write()
# print(text1)                 ---> create a new file
# file1.close()




# file1 = open('myfile1.txt' , 'a')

# file1.write("Hello World!")
# file1.close()

# file1 = open('myfile1.txt' , 'a')

# file1.write("Programming Makes the life Intresting!")
# file1.close()


# with 


with open('myfile1.txt' , 'a') as file:
    file.write("Are you Insane?")
