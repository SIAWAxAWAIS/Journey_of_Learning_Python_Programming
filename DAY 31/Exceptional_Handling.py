# a = input("Enter a Number:")
# print(f"Multiplicatoin Table of {a} is:-")

# try:
#     for i in range(1 , 11):
#         print(f"{int(a)} x {i} = {int(a) *i}")
# except Exception as e:
#     print(e)


try:
    a= int(input("Enter an Number: "))
    print(a)
    x = [5,4]
    print(x[a])
except ValueError:
    print("Number entered is not an Integer.")

except IndexError:
    print("Invalid Index")