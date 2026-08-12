# number = [56,77,61,63,79,48,44]

# index = 0
# for num in number:
#     print(num)
#     if(index ==4):
#         print("Zindabad! Bhai")
#     index = index +1

# enumerate fuction
# for  index ,num in enumerate(number):
#     print(num)
#     if(index == 4):
#         print("Kamal! Shahbash")


country = ["Spain" , "Argentina" , "France" , "Brazil" , "Norway" , "England" , "Protugal" , "Crotia" , "Morocoo"]

for index,con in enumerate(country , start =3):
    print(con)
    if(index == 6):
        print("Brazil is Defeted by Norway! Earling Halland")