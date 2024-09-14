dechiper = input()
comand = input()
while "For Azeroth" != comand:
    comands = comand.split()
    if comands[0] == "GladiatorStance":
        dechiper = dechiper.upper()
        print(dechiper)
    elif comands[0] == "DefensiveStance":
        dechiper = dechiper.lower()
        print(dechiper)
    elif comands[0] == "Dispel":
        index = int(comands[1])
        letter = comands[2]
        if 0< index < len(dechiper):
            dechiper = dechiper.replace(dechiper[index], letter, 1)
            print("Success!")
        else:
            print("Dispel too weak.")
    elif comands[1] == "Change":
        first_subs = comands[2]
        second_subs = comands[3]
        if first_subs in dechiper:
            dechiper = dechiper.replace(first_subs, second_subs)
            print(dechiper)
        else:
            print(dechiper)

    elif comands[1] == "Remove":
        subs = comands[2]
        if subs in dechiper:
            dechiper = dechiper.replace(subs,"")
            print(dechiper)
    else:
        print("Command doesn't exist!")
    comand = input()
# print("For Azeroth")