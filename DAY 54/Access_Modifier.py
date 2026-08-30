# Public

# class Player:
#     def __init__(self):
#         self.name = "Lamin Yamal"

# a = Player()
# print(a.name)


# Private


# class Player:
#     def __init__(self):
#         self.__name = "Cristiano Ronaldo"

# p = Player()
# # print(p.__name) --> cannot access directly
# print(p._Player__name) # it is named as name mangling #--> can be access indirectly
 # print(p.__dir__())

# Protected

class Student:
    def __init__(self, name):
        self._name = name 

class csStudent(Student):
    def display(self):
        
        print(self._name)


obj = csStudent("Zara")
# obj.display() 

print(obj._name)  


