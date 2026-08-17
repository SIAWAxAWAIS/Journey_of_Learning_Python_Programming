# x = 5
# print(x)

# def hy():
#     x = 9
#     print(f"{x} The is Local x")
#     print("Hello World")

# hy()
# print(f"{x} This is Global x")


x = 8

def func():
    global x
    x = 5
    y = 10
    print(y)

func()
print(x)
# print(y) ----> Throws an error

