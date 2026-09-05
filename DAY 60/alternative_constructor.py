class Employee:
    def __init__(self , name , salary):
        self.name = name
        self.salary = salary
    @classmethod
    def fromStr(self , string):
        return self(string.split("-")[0] , int(string.split("-")[1]))


e1 = Employee("Nasir" , 10000)
print(e1.name)
print(e1.salary)

# str = "Nasir-10000"
# e1 = Employee(str.split("-")[0] , str.split("-")[1])
# print(e1.name)
# print(e1.salary)  -->>>> Alternative is given below



string = "Nasir-10000"
e1 = Employee.fromStr(string)
print(e1.name)
print(e1.salary)
