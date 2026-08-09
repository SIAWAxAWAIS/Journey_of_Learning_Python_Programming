# a = int(input("Enter a Number between 0 to 10: "))

# if(a>0 or a<10):
#     raise ValueError("The Number is not between 0 and 10 ")

def value():
    while True:
        u = input("Enter a Number between 0 and 10: ")
        if u == 'quit':
            print("quit does not show any error")
            return
        elif not u.isdigit():
            print("only quit will be printed! Please Enter only quit")
        else:
            num = int(u)
            if 0< num < 10:
                return
            else:
                raise ValueError("Enter a number only between 0 and 10")

try:
    value()
except ValueError as e:
    print("There is an Error which is--->" ,e)

