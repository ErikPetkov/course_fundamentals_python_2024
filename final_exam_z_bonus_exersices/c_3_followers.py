my_dict = {}
comand = input()
while comand != "Log out":
    comand = comand.split()
    if "New" == comand[0]:
        username = comand[2]
        if username not in my_dict.keys():
            my_dict[username] = {
                "likes":0, "comm":0
            }
    elif "Like:" == comand[0]:
        username = str(comand[1])
        username = username.replace(":","")
        count = int(comand[2])
        if username in my_dict.keys():
            my_dict[username]["likes"]+=count
        else:
            my_dict[username] = {"likes":count, "comm":0}

    elif "Comment:" == comand[0]:
        username = comand[1]
        if username in my_dict.keys():
            my_dict[username]["comm"] += 1
        else:
            my_dict[username] = {"likes": 0, "comm": 1}
    elif "Blocked:" == comand[0]:
        username = comand[1]
        if username in my_dict.keys():
            del my_dict[username]
        else:
            print(f"{username} doesn't exist.")
    comand = input()
count = len(my_dict.keys())
print(f"{count} followers")
for key in my_dict.keys():
    print(f"{key}: {my_dict[key]['likes']+my_dict[key]['comm']}")