password = input()
list_let = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
comands = input().split()
while "Complete" != comands[0]:
    if "Upper" in comands:
        index = int(comands[2])
        pas = ""
        l_u = ""
        for i in range(len(password)):
            if  password[i].lower() in list_let and l_u == "" and not password[i].isdigit() and index == i:
                ll = password[i].upper()
                l_u = ll
                pas+= ll
            else:
                pas += password[i]
        password = pas
        print(password)
    elif "Lower" in comands:
        index = int(comands[2])
        pas = ""
        l_u = ""
        for i in range(len(password)):
            if password[i].lower() in list_let and l_u == "" and not password[i].isdigit() and index == i:
                ll = password[i].lower()
                l_u = ll
                pas+= ll
            else:
                pas += password[i]
        password = pas
        print(password)

    elif "Insert" == comands[0]:
        index = int(comands[1])
        char = comands[2]
        if char.isdigit() or char.lower() in list_let or char == "_":
            password = password[:index]+char+password[index:]
            print(password)

    elif "Replace" == comands[0]:
        char = comands[1]
        value = int(comands[2])
        if char in password:
            value += ord(char)
            nue_char = chr(value)
            password = password.replace(char, nue_char)
            print(password)
    elif "Validation" == comands[0]:
        if len(password) < 8:
            print("Password must be at least 8 characters long!")
        for char in password:
            if not char.isdigit() and not char.lower() in list_let and char != "_":
                print("Password must consist only of letters, digits and _!")
                break
        up_l = ""
        for l in list_let:
            if l.upper() in password:
                up_l+=l
        if len(up_l) < 1:
            print("Password must consist at least one uppercase letter!")
        lw_l = ""
        for l in list_let:
            if l in password:
                lw_l += l
        if len(lw_l) < 1:
            print("Password must consist at least one lowercase letter!")
        d_t = ""
        for char in password:
            if char.isdigit():
                d_t+=char
        if len(d_t)<=1:
            print("Password must consist at least one digit!")
    comands = input().split()
