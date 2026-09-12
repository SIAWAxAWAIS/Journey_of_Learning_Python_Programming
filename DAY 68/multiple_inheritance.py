class Singer:
    def __init__(self, name):
        self.name = name

    def show(self):
        print(f"The name of the Singer is {self.name}")


class Dancer:
    def __init__(self, typeDance):
        self.typeDance = typeDance

    def show(self):
        print(f"The dance type is {self.typeDance}")



class SingerDancer(Singer, Dancer):
    def __init__(self, name, typeDance):
        Singer.__init__(self, name)
        Dancer.__init__(self, typeDance)


o = SingerDancer("Shakira", "Belly Dance")
print(o.name)
print(o.typeDance)
o.show()
print(SingerDancer.mro()) # MRO stands for method resolution order