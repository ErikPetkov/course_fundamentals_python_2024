gifts = input().split()
command = input()
while command != "No Money":
    line = command.split()
    if line[0] == "OutOfStock":
        for i in range(len(gifts)):
            if gifts[i] == line[1]:
                gifts[i] = "None"
    elif line[0] == "Required":
        index = int(line[2])
        try:
            gifts[index] = line[1]
        except:
            pass
        # if index >= 0 and index < len(gifts):
        #     gifts[index] = line[1]
    elif line[0] == "JustInCase":
        gifts[-1] = line[1]
    command = input()

for gift in gifts:
    if gift != "None":
        print(gift, end=' ')
