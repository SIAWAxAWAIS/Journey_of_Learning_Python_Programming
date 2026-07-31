countries = ("Spain" , "Argentina", "Italy" , "France" , "Brazil" , "Noway" , "England" , "Protugle" , "Morocoo" , "Japan")

tup2 = list(countries)
tup2.append("Russia")
countries = tuple(tup2)
print(countries)

res =countries.count("Spain")
print("There are ",res," Count of country")


instant = (1,5,473,5,47,4,1,7,4)
print(instant.index(4))
print(instant.index(5 , 2 ,5))