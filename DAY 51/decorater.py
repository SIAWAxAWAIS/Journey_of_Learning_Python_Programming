def greet(fx):
    def mfx(*args , **kwargs):
        print("Happy Good Morning")
        fx(*args , **kwargs)
        print("Thanks! May Your Day Passes Good")
    return mfx

@greet
def hello():
    print("Hello World")

@greet
def add(a , b):
    print(a+b)

hello()
add(2 ,5)