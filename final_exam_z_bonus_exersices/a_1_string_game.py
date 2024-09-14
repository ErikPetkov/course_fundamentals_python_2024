strin = input()
comand = input().split()
while "Done" not in comand:
    if "Change" == comand[0]:
        char = comand[1]
        repl = comand[2]
        strin = strin.replace(char, repl)
        print(strin)

    elif "Includes" == comand[0]:
        subs = comand[1]
        if subs in strin:
            print("True")
        else:
            print("False")

    elif "End" == comand[0]:
        subs = comand[1]
        if subs == strin[-len(subs):]:
            print("True")
        else:
            print("False")

    elif "Uppercase" == comand[0]:
        strin = strin.upper()
        print(strin)

    elif "FindIndex" == comand[0]:
        char = comand[1]
        ind = 0
        for i in range(len(strin)):
            if strin[i] == char:
                ind = i
                break
        print(ind)

    elif "Cut" == comand[0]:
        start_index = int(comand[1])
        count = int(comand[2])
        colect = ("")
        for i in range(len(strin)):
            if start_index <= i <= start_index+count-1:
                colect+= strin[i]
        print(colect)

    comand = input().split()

