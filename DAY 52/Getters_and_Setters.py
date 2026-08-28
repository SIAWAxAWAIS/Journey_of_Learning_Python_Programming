class myClass:
    def __init__(self , value):
        self._value = value

    def show(self):
        print(f"Value is {self._value}")

    @property
    def new_value(self):
        return 10 * self._value
    
    @new_value.setter
    def new_value(self , be_value):
        self._value = be_value / 10
obj = myClass(5)
# print(obj.new_value)
obj.new_value = 100
print(obj.new_value)
obj.show()