class man:
    name = "Asad"
    age = 16
    occupation = "Software Developer"
    def info(self):
        print(f"{self.name} is {self.age} year old and he/she is {self.occupation}")
    



x = man()
y = man()
x.name = "Qalandar"
x.age = 18
x.occupation = "AI / Machine Learner"

y.name = "Rania"
y.age = 20
y.occupation = "Senior Software Developer"


x.info()
y.info()