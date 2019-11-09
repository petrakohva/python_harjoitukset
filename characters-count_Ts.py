def main(uInput):
    count = 0
    for letter in uInput:
        if letter == "t":
            count += 1
    print(count)

main(input("Anna merkkijono: ").lower())
    
