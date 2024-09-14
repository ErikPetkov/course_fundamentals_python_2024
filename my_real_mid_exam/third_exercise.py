chat = list()
comand = input().split()
while "end" not in comand:
    if "Chat" in comand:
        chat.append(comand[1])
    elif "Delete" in comand:
        if comand[1] in chat:
            chat.remove(comand[1])
    elif "Edit" in comand:
        if comand[1] in chat:
            a = chat.index(comand[1])
            chat.insert(a, comand[2])
            chat.remove(comand[1])
    elif "Pin" in comand:
        if comand[1] in chat:
            chat.remove(comand[1])
            chat.append(comand[1])
    elif "Spam" in comand:
        comand.remove("Spam")
        for c in comand:
            chat.append(c)
    comand = input().split()
for l in chat:
    print(l)