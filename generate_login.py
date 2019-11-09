from login import get_login_name
def main():
    firstName = input("Enter your first name: ")
    lastName = input("Enter your last name: ")
    idNumber = input("Enter your student ID number: ")
    return print("Your system login name is: \n" + get_login_name(firstName, lastName, idNumber))
main()
