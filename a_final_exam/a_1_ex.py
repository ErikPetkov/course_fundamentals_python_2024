spell = input()
comand = input().split()
while "Abracadabra" != comand[0]:
    if "Abjuration" == comand[0]:
        spell = spell.upper()
        print(spell)
    elif "Necromancy" == comand[0]:
        spell = spell.lower()
        print(spell)
    elif "Illusion" == comand[0]:
        index = int(comand[1])
        letter = comand[2]
        if index >= len(spell) or index < 0:
            print("The spell was too weak.")
        else:
            spell = spell.replace(spell[index], letter)
            print("Done!")
    elif "Divination" == comand[0]:
        f_subs = comand[1]
        s_subs = comand[2]
        if f_subs in spell and s_subs != "":
            spell = spell.replace(f_subs, s_subs)
    elif "Alteration" == comand[0]:
        subs = comand[1]
        if subs in spell:
            spell = spell.replace(subs,"")
            print(spell)
    else:
        print("The spell did not work!")
    comand = input().split()

