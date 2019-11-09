print("KPH\t\tMPH")
print("--------------------")
for speed in range(60,131,10):
    print(str(speed) + "\t\t" + str(round(speed*0.62137,1)))
    
