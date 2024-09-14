comand = input().split("-")
dict = {}
while len(comand) != 1:
    key, value = comand
    dict[key] = value
    comand = input().split("-")
number = int(comand[0])

for n in range(number):
    name = input()
    if name in dict:
        print(f"{name} -> {dict[name]}")
    else:
        print(f"Contact {name} does not exist.")