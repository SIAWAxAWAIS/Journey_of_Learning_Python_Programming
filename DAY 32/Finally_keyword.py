def func():
    try:
        l = [1,3,2,7]
        i = int(input("Enter a Index Number: "))
        print(l[i])
        return 1
    except:
        print("Index out of Bound")
        return 0
    finally:
        print("I am Finally and I will always be executed!")

a = func()
print(a)