user = input("Type your User: ")
password = input("Type your Password: ")

while user == password:
    user = input("Invalid Password! \nPlease Type a valid user and password! \nType your User: ")
    password = input("Type your Password: ")

print("Login Ok!")