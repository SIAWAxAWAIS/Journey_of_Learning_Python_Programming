# class ParentClass:
#     def p_method(self):
#         print("This is the Parent Class Method")

# class ChildClass(ParentClass):
#     def c_class(self):
#         print("This is a child Class")
#         super().p_method()

# childObject = ChildClass()
# childObject.c_class()


class Employee:
    def __init__(self , name , id):
        self.name = name
        self.id = id

class Programmer(Employee):
    def __init__(self , name , id , pLang):
        super().__init__(name , id)
        self.pLang = pLang
        

emp = Employee("Zahid" , 84)
prog = Programmer("Zaman Baba" , 76 , "C++")
print(prog.pLang)
