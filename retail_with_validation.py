choise = "y"
while choise == "y":
    cost = float(input("Enter the item's wholesale cost: "))
    while cost <=  0:
        print("ERROR: the cost cannot be zero or negative")
        cost = float(input("Enter the correct wholesale cost: "))
    print("Retail price: $" + str(cost*2.5))
    choise = input("Do you have another item? (Enter Y for yes): ")

