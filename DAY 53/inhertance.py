class Employee:
    def __init__(self , name , id):
        self.name = name
        self.id = id

    def showDetails(self):
        print(f"The name of the Employee is: {self.name} and has {self.id} ID")

class Occupation(Employee):
    def showOccuption(self):
        print(f"The occuption is Software Developer")


e = Occupation("Ali" , 420)
e.showDetails()
e.showOccuption()