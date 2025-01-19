# Upper or lowercases of all sentances

action= input("Press (u) for uppercase and (l) for lowercases:")
name = input("Please enter your text:")

if  action == "u":
     name = name.upper()
     print(name)
elif action == "l":
    name = name.lower()
    print(name)


