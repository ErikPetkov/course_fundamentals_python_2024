encrupted_message = input()
comand = input().split("|")
while "Decode" not in comand:
    mission = comand[0]
    if "Move" == mission:
        num_letters = int(comand[1])
        encrupted_message = encrupted_message[num_letters:]+ encrupted_message[:num_letters]
    elif "Insert" == mission:
        index = comand[1]
        value = comand[2]
        encript = ""
        for i in range(len(encrupted_message)):
            if i == int(index):
                encript += value
            encript += encrupted_message[i]
        encrupted_message = encript
        if value not in encrupted_message:
            encrupted_message+=value
    elif "ChangeAll" == mission:
        subs = comand[1]
        repl = comand[2]
        encrupted_message = encrupted_message.replace(subs, repl)
    comand = input().split("|")

print(f"The decrypted message is: {encrupted_message}")