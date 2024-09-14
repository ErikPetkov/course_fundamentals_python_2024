hearoes = {}
comand = input().split()
while "End" not in comand:
    if "Enroll" == comand[0]:
        hero_name = comand[1]
        if hero_name in hearoes.keys():
            print(f"{hero_name} is already enrolled.")
        else:
            hearoes[hero_name] = []

    elif "Learn" == comand[0]:
        hero_name = comand[1]
        spell_name = comand[2]
        if hero_name in hearoes.keys():
            if spell_name not in hearoes[hero_name]:
                hearoes[hero_name].append(spell_name)
            else:
                print(f"{hero_name} has already learnt {spell_name}.")
        else:
            print(f"{hero_name} doesn't exist.")
    elif "Unlearn" == comand[0]:
        hero_name = comand[1]
        spell_name = comand[2]
        if hero_name in hearoes.keys():
            if spell_name in hearoes[hero_name]:
                hearoes[hero_name].remove(spell_name)
            else:
                print(f"{hero_name} doesn't know {spell_name}.")
        else:
            print(f"{hero_name} doesn't exist.")
    comand = input().split()

print("Heroes:")
for hero_name,spell_name in hearoes.items():
    print(f"== {hero_name}: " +" ,".join(spell_name))

