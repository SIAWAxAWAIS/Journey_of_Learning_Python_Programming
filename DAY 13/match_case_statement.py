x = int(input("Enter the value of x:"))

match x:
    case 0 :
        print("x is Zero")
    case 1 :
        print("x is Positve")
    case 2 :
        print("x is negative")
    case _:
        print("Invalid Statement")


# Positve,negative and zero determination using match

x = int(input("Enter the value of x:"))

match x:
    case _ if x==0:
        print("x is Zero")
    case _ if x>0:
        print("x is Positve")
    case _ if x<0:
        print("x is negative")
    

