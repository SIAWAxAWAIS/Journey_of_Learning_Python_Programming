class Employee:
    company = "Google"
    def show(self):
        print(f"The name of the Employee is {self.name} and the company name is {self.company}")

    @classmethod
    def changeCompany(cls , newCompany):
        cls.company = newCompany

e1 = Employee()
e1.name = "Chris"
e1.changeCompany("Microsoft")
e1.show()
print(Employee.company)
