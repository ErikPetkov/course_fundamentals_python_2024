textt = input()

password = ""
while True:
    comand = input().split()
    if "Done" in comand:
        break
    if comand[0] == "TakeOdd":

        for i in range(len(textt)):
            if i % 2 == 1:
                password+= textt[i]
        print(password)
    elif comand[0] == "Cut":

        index = comand[1]
        lenght = comand[2]
        t = ""
        for i in range(len(password)):
            if i >= int(index) and i <= int(index)+int(lenght):
                pass
            else:
                t += password[i]
        password = t
        print(password)
    elif comand[0] == "Substitute":
        substring = comand[1]
        subtitule = comand[2]
        if substring in password:
            a = 0
            while substring in password:
                for i in substring:
                    if 1 == len(substring):
                        password = password.replace(i, subtitule)
                    else:
                        a+=1
                        if a == len(substring):
                            password = password.replace(i, subtitule,1)
                            a = 0
                        else:
                            password = password.replace(i,"",1)
            print(password)
        else:
            print("Nothing to replace!")




print(f"Your password is: {password}")