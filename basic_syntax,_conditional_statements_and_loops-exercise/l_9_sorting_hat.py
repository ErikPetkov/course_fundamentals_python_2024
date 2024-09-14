name = input()
vol = False
while name != "Welcome!":
    if len(name) <= 4:
        print(f"{name} goes to Gryffindor.")
    elif len(name) == 5:
        print(f"{name} goes to Slytherin.")
    elif len(name) == 6:
        print(f"{name} goes to Ravenclaw.")
    elif name == "Voldemort":
        print("You must not speak of that name!")
        vol = True
        break
    elif len(name) > 6:
        print(f"{name} goes to Hufflepuff.")
    name = input()
if vol == False:
    print("Welcome to Hogwarts.")