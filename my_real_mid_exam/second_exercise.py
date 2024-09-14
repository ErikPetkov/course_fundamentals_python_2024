cofees = input().split()
iterations = int(input())
for i in range(iterations):
    comand = input().split()
    if "Include" in comand:
        cofees.append(comand[1])
    elif "Remove" in comand:
        if len(cofees) <= 2:
            pass
        else:
            if comand[1] == "first":
                for _ in range(int(comand[2])):
                    cofees.remove(cofees[0])
            else:
                for _ in range(int(comand[2])):
                    cofees.remove(cofees[-1])
    elif "Prefer" in comand:
        co = int(comand[1])
        com = int(comand[2])
        if co < 0 or co > len(cofees)-1:
            pass
        elif com < 0 or com > len(cofees)-1:
            pass
        else:
            if cofees[co] in cofees and cofees[com] in cofees:
                cofees[co], cofees[com] = cofees[com], cofees[co]
    elif "Reverse" in comand:
        cofees.reverse()
print("Coffees:")
print(" ".join(cofees))
