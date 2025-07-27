#4.Accept name and age from the user. Check if the user i a valid voter or not! ❤️❤️
name = input("Give me a name:- ")
age = int(input("Give me a age number:-"))

if age >=18:
    print(f"hi {name}, this is valid voter!")
elif age <= 18:
    print(f"hi {name},Ok this is sometiems voter in the city")
else:
    print(f"{name}, this not voter")