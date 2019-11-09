def get_login_name(firstName, lastName, idNumber):
    return firstName[0:3] + lastName[0:3] + idNumber[-3:]
