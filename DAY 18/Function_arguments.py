def avg(a=9 , b=6):
    print("The average is :" , (a+b)/2)

# avg(4,6)
avg()


def name(fn,sn,tn):
    print("Hello," ,fn ,sn , tn)

name("Ali" , "Raza" , "Ahmad")


# for multiple arguments

# def averge(*num):
#     sum =0
#     for i in num:
#         sum = sum +i
#     print("Averge is equal to : " , sum / len(num))

# averge(6,4,5,5)

# for dictonary

def name(**name):
    print("Hello ," ,name["fn"] , name["sn"] , name["tn"])

name(fn = "Call of Duty" , sn = "GTA 6" , tn = "Resident Evil 9 Requiem")


# return statement

def average(*numbers):
    sum =0
    for i in numbers:
        sum = sum + i
    return sum / len(numbers)

a = average(6,4)
print(a)