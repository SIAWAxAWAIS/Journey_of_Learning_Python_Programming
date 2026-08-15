import os

if(not os.path.exists("Data")):
    os.mkdir("Data") #  --> create Data folder

for i in range(0,100):
    os.mkdir(f"Data/Day{i+1}") # --> Create 100 folders in Data