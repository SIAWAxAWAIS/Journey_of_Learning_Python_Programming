# Union and Update

# set1 = {7,5,4,9,0,3}
# set2 = {7,4,9,2,6}
# print(set1.union(set2))
# set1.update(set2)
# print(set1 , set2)

# intersection and update

# city1 = {"France" , "Japan" , "Germany" , "Spain" , "China" , "Netherlands"}
# city2 = {"Pakistan" , "Argentina", "Netherlands" , "England" , "Spain" , "America"}

# print(city1.intersection(city2))
# city1.update(city2)
# print(city1 , city2)

# symmetric diffrence


# city1 = {"France" , "Japan" , "Germany" , "Spain" , "China" , "Netherlands"}
# city2 = {"Pakistan" , "Argentina", "Netherlands" , "England" , "Spain" , "America"}

# print(city1.symmetric_difference(city2))


# Diffrence 


# city1 = {"France" , "Japan" , "Germany" , "Spain" , "China" , "Netherlands"}
# city2 = {"Pakistan" , "Argentina", "Netherlands" , "England" , "Spain" , "America"}

# print(city1.difference(city2))


# disjoints sets


# city1 = {"France" , "Japan" , "Germany" , "Spain1" , "China" , "Netherlands1"}
# city2 = {"Pakistan" , "Argentina", "Netherlands" , "England" , "Spain" , "America"}

# print(city1.isdisjoint(city2))


# superset


# city1 = {"France" , "Japan" , "Germany" , "Spain" , "China" , "Netherlands"}
# city2 = {"Netherlands" , "Spain"}

# city3 = city1.issuperset(city2)
# print(city3)


# add and remove and  discard


# name = {"Aslam" , "Umer" , "Ali" , "Aslan"}
# name.add("Abdullah")
# print(name)


# name = {"Aslam" , "Umer" , "Ali" , "Aslan"}
# name.remove("Ali")
# print(name)



# name = {"Aslam" , "Umer" , "Ali" , "Aslan"} --> not shows any error
# name.discard("Arslan")
# print(name)



# pop

# num = {1,5,7,3}
# print(num.pop())


# del

# num = {1,5,7,3}
# del num 
# print(num) --> Throws and error

# clear

# num = {1,5,7,3}
# num.clear() 
# print(num)


city1 = {"France" , "Japan" , "Germany" , "Spain" , "China" , "Netherlands"}
if "Spain" in city1:
    print("Spain won the World Cup")
else:
    print("Argentina loss the World Cup by Spain")