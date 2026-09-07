# a = [18,17,16]
# print(dir(a))
# print(a.__add__)


class Employee:
    def __init__(self , name , age):
        self.name = name
        self.age = age

e = Employee("Haris" , 20)
print(e.__dict__)
print(e.name , e.age)

# Help of Class Employee

print(help(Employee))

# class Employee(builtins.object)
#  |  Employee(name, age)
#  |
#  |  Methods defined here:
#  |
#  |  __init__(self, name, age)
#  |      Initialize self.  See help(type(self)) for accurate signature.
#  |
#  |  ----------------------------------------------------------------------
#  |  Data descriptors defined here:
#  |
# -- More  --