# x = int(input("Enter your age: "))
# print("Your age is ",x)


# if else

x = int(input("Enter your age: "))
if(x>=18):
    print("You can drive a car.")
else:
    print("You can not drive a car")


# if else elif

num = int(input("Enter a number: "))
if(num>0):
    print("The number is positive")
elif(num<0):
    print("The number is negative")
else:
    print("The number is zero")


# nested if

num = 17

if(num!=17):
    print("You can eat pizza")
elif(num<20):

    if(num<50):
        print("i am good")
    elif(num==20):
        print("i am sad")
    else:
        print("May, You live long")

elif(num==20 and num==70):
    print("you may go right now")
else:
    print("you should sleep a head now")