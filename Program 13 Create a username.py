# Create a username
# Rules
# 1. Username is no more than 12 characters
# 2. username must not contain spaces
# 3. username must not contain any digits

name= input("Enter new username: ")

if len(name) > 12:
    print("Your username can't be more than 12 characters")

elif not name.find(" ") == -1:
    print("Your username can't contain any spaces")

elif not name.isalpha():
    print("Your username cannot include any digits")

else:
    print(f"Your username has been created, welcome: {name}. ")