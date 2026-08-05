dict = {
    "Name": "Awais",
    "Roll No": "13",
    "Class" : "12"
}
# print(dict["Name"])
# print(dict["Roll No"])
# print(dict["Class"])
# print(dict)
# print(dict["Name1"]) --> Throws Error 
# print(dict.get("Name1"))  --> Throws None

# print(dict.keys() , dict.values())

# for key in dict.keys():
#     print(dict[key])

print(dict.items())
for key,value in dict.items():
    print(f"The value of Key {key} according to the values is {value}")