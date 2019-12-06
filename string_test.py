def tyyppi_test():
    userFeed = input("Enter a string: ")
    vastaus = "This is what I found about that string:"
    if userFeed.isalnum():
        vastaus += "\nThe string is alphanumeric."
        if userFeed.isalpha():
            vastaus += "\nThe string contais only alphabetic characters."
        elif userFeed.isdigit():
            vastaus += "\nThe string contais only digits"
        if userFeed.islower():
            vastaus +="\nThe letters in the string are all lowercase."
        elif userFeed.isupper():
            vastaus +="\nThe letters in the string are all uppercase."
    return print(vastaus)

tyyppi_test()
