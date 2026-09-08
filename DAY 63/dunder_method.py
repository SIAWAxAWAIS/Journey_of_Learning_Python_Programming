# __len__
# class Queen:
#     name = "Princess Leonar"
#     def __len__(self):
#         i = 0
#         for c in self.name:
#             i = i +1
#         return i

# e = Queen()
# print(e.name)
# print(len(e))


# __init__
# class Queen:
#     def __init__(self , name):
#         self.name = name
    
#     def __len__(self):
#         i = 0
#         for c in self.name:
#             i = i +1
#         return i

# e = Queen("Princess Leonar")
# print(e)


# __str__
# class Queen:
#     def __init__(self , name):
#         self.name = name
    
#     def __len__(self):
#         i = 0
#         for c in self.name:
#             i = i +1
#         return i

#     def __str__(self):
#         return f"The name of the Queen of Spain is: {self.name}"

# e = Queen("Princess Leonar")
# print(e)


# __repr__
# class Queen:
#     def __init__(self , name):
#         self.name = name
    
#     def __len__(self):
#         i = 0
#         for c in self.name:
#             i = i +1
#         return i

#     def __str__(self):
#         return f"The name of the Queen of Spain is: {self.name}"

#     def __repr__(self):
#         return f"Same as Above The name of Queen Austrias ('{self.name}')"

# e = Queen("Princess Leonar")
# print(str(e))
# print(repr(e))



# __call__
class Queen:
    def __init__(self , name):
        self.name = name
    
    def __len__(self):
        i = 0
        for c in self.name:
            i = i +1
        return i

    def __str__(self):
        return f"The name of the Queen of Spain is: {self.name}"

    def __call__(self):
        print("Hey Hello World")

e = Queen("Princess Leonar")
e()