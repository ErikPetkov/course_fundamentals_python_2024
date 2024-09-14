key = input()
dict = {}
while key != "stop":
    value = int(input())
    if key in dict:
        dict[key]+=value
    else:
        dict[key] = value
    key = input()

for key in dict.keys():
    print(f"{key} -> {dict[key]}")