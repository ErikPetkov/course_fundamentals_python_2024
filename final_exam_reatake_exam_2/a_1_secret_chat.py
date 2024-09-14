cripted_mesage = input()
comand = input().split(":|:")
while "Reveal" not in comand:
    mission = comand[0]
    if "InsertSpace" == mission:
        index = comand[1]
        crip = ""
        for i in range(len(cripted_mesage)):
            if i == int(index):
                crip += " "
            crip+= cripted_mesage[i]
        cripted_mesage = crip
        print(cripted_mesage)

    elif "Reverse" == mission:
        subs = comand[1]
        if subs in cripted_mesage:
            r_subs = subs[::-1]
            cripted_mesage = cripted_mesage.replace(subs,"",1)+r_subs
            print(cripted_mesage)
        else:
            print("error")

    elif "ChangeAll" == mission:
        subs = comand[1]
        replacement = comand[2]
        cripted_mesage = cripted_mesage.replace(subs,replacement)
        print(cripted_mesage)

    comand = input().split(":|:")

print(f"You have a new text message: {cripted_mesage}")