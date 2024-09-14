comand = input()
my_dict = {}
while comand != "Results":
    comands = comand.split(":")
    if comands[0] == "Add":
        person_name = comands[1]
        healt = int(comands[2])
        energy = int(comands[3])
        if person_name in my_dict.keys():
            my_dict[person_name]["health"] += healt

        else:
            my_dict[person_name] ={"health":healt, "energy":energy}
    elif comands[0] == "Attack":
        atacker_name = comands[1]
        defender_name = comands[2]
        damage = int(comands[3])
        if atacker_name in my_dict and defender_name in my_dict:
            my_dict[defender_name]["health"] -= damage
            my_dict[atacker_name]["energy"] -= 1
            if my_dict[defender_name]["health"] <= 0:
                print(f"{defender_name} was disqualified!")
                del my_dict[defender_name]
            if my_dict[atacker_name]["energy"] <= 0:
                print(f"{atacker_name} was disqualified!")
                del my_dict[atacker_name]
    elif comands[0] == "Delete":
        username = comands[1]
        if username == "All":
            del my_dict
        else:
            my_dict.clear()
    comand = input()
print(f"People count: {len(my_dict.keys())}")
for key in my_dict.keys():
    print(f"{key} - {my_dict[key]['health']} - {my_dict[key]['energy']}")