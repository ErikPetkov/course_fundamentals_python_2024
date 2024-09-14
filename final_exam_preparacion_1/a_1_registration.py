username = input()
comand = input()
while comand != "Registration":
    comand = comand.split()
    if comand[0] == "Letters":
        if comand[1] == "Upper":
            username = username.upper()
        else:
            username = username.lower()
        print(username)
    elif comand[0] == "Reverse":
        start_index, end_index = int(comand[1]), int(comand[2])+1
        if 0 <= start_index < len(username) and 0 <= end_index < len(username):
            print(username[start_index:end_index:][::-1])
    elif comand[0] == "Substring":
        sub_str = comand[1]
        if sub_str in username:
            print(username.replace(sub_str,""))
        else:
            print(f"The username {username} doesn't contain {sub_str}.")
    elif comand[0] == "Replace":
        while comand[1] in username:
            username = username.replace(comand[1],"-")
        print(username)

    elif comand[0] == "IsValid":
        if comand[1] in username:
            print("Valid username.")
        else:
            print(f"{comand[1]} must be contained in your username.")
    comand = input()