num_wagons = int(input())
wagon = [0] * num_wagons
comand = input().split(" ")
while True:
    if "add" in comand:
        wagon[-1] += int(comand[1])
    elif "insert" in comand:
        wagon[int(comand[1])] += int(comand[2])
    elif "leave" in comand:
        wagon[int(comand[1])] -= int(comand[2])
    if comand[0] == "End":
        break
    comand = input().split()
print(wagon)