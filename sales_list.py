list = [0]*5
i=0
print("Enter the sales of each day")
while i < len(list):
    list[i] = input("Day #"+ str(i+1) + ": ")
    i+=1

print("Here are the values you entered:")
for value in list:
    print(round(float(value),1))
