# class person:
#     name = "Ronaldo"
#     occupation = "Portugal Footballer"
#     def info(self):
#         print(f"{self.name} is a {self.occupation}")

# a = person()
# b= person()
# c = person()
# b.name = "Lamine Yamal"
# b.occupation = "Spanish Footballer"
# c.name = "Leo Messi"
# c.occupation = "Argentinian Footballer"
# a.info()
# b.info()
# c.info()


class person:
    def __init__(self ,name ,occupation):
        print("Lamine Yamal is a Spanish Footballer")
        print("Leo Messi is a Argentinian Footballer")
        print("Cristiano Ronaldo is a Portugal Footballer")
        print("Earling Halland is a Norwian Footballer")
        self.name = name
        self.occupation = occupation

    def info(self):
        print(f"{self.name} is  {self.occupation}")

a= person("Call of Duty Modern Warfare 4 2026" , "Made by infinity Ward")

a.info()
