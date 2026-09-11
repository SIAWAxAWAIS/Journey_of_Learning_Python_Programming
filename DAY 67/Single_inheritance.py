class Animal:
    def __init__(self , name , species):
        self.name = name
        self.species = species

    def make_sound(self):
        print("Sound is made by the Animals")

# class Dog(Animal):
#     def __init__(self , name , breed):
#         Animal.__init__(self, name , species="Dog")
#         self.breed = breed

#     def make_sound(self):
#         print("Bark")
class Cat(Animal):
    def __init__(self , sound , walk):
        self.sound = sound
        self.wald = walk

# d = Dog("Puppy" , "Dog")
# d.make_sound()

# a = Animal("Zabra" , "Forest Animal")
# a.make_sound()

c = Cat("Meow" , "On four legs")
print(c.sound)
# c.make_sound()