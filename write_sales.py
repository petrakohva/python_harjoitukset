todo_file = open('sales.txt', 'w')
days = int(input("For how many days do you have sales? "))
counter = 1
while counter <= days:
    sales = input("Enter the sales for day #" + str(counter) + ": ")
    counter += 1
    todo_file.write((sales) + "\n")
todo_file.close()
print("Data written to sales.txt")
