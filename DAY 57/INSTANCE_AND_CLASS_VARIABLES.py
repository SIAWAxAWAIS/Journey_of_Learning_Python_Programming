class Employee:
    companyName = "Ultimate Coding Studio"
    noOfEmployees = 0
    def __init__(self , name):
        self.name = name
        self.id = 5683
        Employee.noOfEmployees += 1
    def showDetails(self):
        print(f"The name of the Employee is {self.name}, the id is {self.id},his/her number of Employee is {self.noOfEmployees} and he/she works in {self.companyName}")

# Employee.showDetails(e)       #instead
e = Employee("Qainat")
e.companyName = "Google"
e.id = 6784
e.showDetails()  
print(e.companyName)
e = Employee("Zara")
e.showDetails()  
