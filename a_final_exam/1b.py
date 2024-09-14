spell = input()
command = input()
while command != "Abracadabra":
    if command == "Abjuration":
        spell = spell.upper()
        print(spell)
    elif command == "Necromancy":
        spell = spell.lower()
        print(spell)
    elif "Illusion" in command:
        command = command.split()
        index, letter = int(command[1]), command[2]
        if index >= len(spell) or index < 0:
            print("The spell was too weak.")
        else:
            spell = spell.replace(spell[index], letter)
            print("Done!")
    elif "Divination" in command:
        _, f_subs, s_subs = command.split()
        if f_subs in spell and s_subs != "":
            spell = spell.replace(f_subs, s_subs)
    elif "Alteration" in command:
        _, subs = command.split()
        if subs in spell:
            spell = spell.replace(subs,"")
            print(spell)
    else:
        print("The spell did not work!")
    command = input()
print(spell)