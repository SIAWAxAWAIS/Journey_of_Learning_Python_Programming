# f  = open("file.txt" , 'r')
# while True:
#     line = f.readline()
#     if not line:
#         break
#     print(line , type(line))


# f  = open("marks.txt" , 'r')
# i = 0
# while True:
#     i += 1
#     line = f.readline()
#     if not line:
#         break
#     l1 = int(line.split(",")[0])
#     l2 = int(line.split(",")[1])
#     l3 = int(line.split(",")[2])
#     print(f"Marks of the Stundent {i} is {l1*2}")
#     print(f"Marks of the Stundent {i} is {l2*2}")
#     print(f"Marks of the Stundent {i} is {l3*2}")
#     print(line , type(line))


f = open("file1.txt" , 'w')
lines = ['Line0\n' , 'Line1\n', 'Line2']
f.writelines(lines)
f.close()

