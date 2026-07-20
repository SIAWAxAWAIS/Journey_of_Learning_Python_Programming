
# A variable can be override in python means you can use same name of variables for diffrent values stored in it

name = "Ahsan"
print(len(name))
print(name.upper()) #Strings are immutable

a = "Hamza!!!!!!!"
print(a.strip("!"))


a1 = "Abdullah"
print(a1.replace("Abdullah" , "Ahad"))

# convert into list
a2 = "Awais Ahmad Abubakar Abdullah"
print(a2.split(" "))

a3 = "awais"
print(a3.capitalize())

blog = "introdution to java,sPringBoot,Microsevices."
print(blog.capitalize())


str1 = "Welcome, To Dubai"
print(len(str1))
print(str1.center(50))
print(len(str1.center(50)))


str2 = "I am in Dubai and i am in Sharjah"
print(str2.count("in"))

#endswith and startswith always return boolean

str3 = "I am in Dubai and i am in Sharjah"
print(str3.endswith("Sharjah"))


str4 = "I am in Dubai and i am in Sharjah"
print(str4.startswith("am")) # returns false


str5 = "I am in Dubai and i am in Sharjah"
print(str5.startswith(" in",4,10))

# To find index of first accurence when not found returns -1 , index is similar to find but it terminates the statement by showing error

str6 = "I am in Dubai and i am in Sharjah"
print(str6.find("and"))


# For alphaNumeric .isalnum  , for Alphabet only .isalpha and for to check lower .islower

str7 = "I am in Dubai and i am in Sharjah"
print(str7.isalnum())  #False because it contains spaces

str8 = "WelcomeGoodMorning"
print(str8.isalnum())      


# For printable character , to check spacint .isspace

x = "i am a boy\n"
print(x.isprintable())  # \n is not a printable chracter


y ="Programming makes the life intresting."
print(y.istitle()) #false

y1 = "Programming Makes The Life Intresting"
print(y1.istitle())

#To converting uppercase to lower or lower to upper


y2 = "Programming Makes The Life Intresting"
print(y2.swapcase())




