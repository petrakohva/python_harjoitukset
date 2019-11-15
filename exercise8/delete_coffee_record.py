
import os
coffee_file = open("coffee.txt", "r")
temp_file = open("tempo.txt", "w")
remove = input("Insert name of the coffee you wish to remove: ")
line = coffee_file.readline()
while line:
    line = line.rstrip("\n")
    if line != remove:
        temp_file.write(line + "\n")
    line = coffee_file.readline()
coffee_file.close()
temp_file.close()

os.remove("coffee.txt")
os.rename("tempo.txt", "coffee.txt")

    
