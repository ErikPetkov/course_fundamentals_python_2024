game_data = input().split()
total = 0
num = 0
for data in game_data:
    data = data.strip()
    num = ""
    for n in data:
        if n.isnumeric():
            num+=n
    num = int(num)
    if data[0].isupper():
        num = num/(ord(data[0])-64)
    elif data[0].islower():
        num = num*(ord(data[0])-96)

    if data[-1].isupper():
        total+= num-(ord(data[-1])-64)
    elif data[-1].islower():
        total+= num+(ord(data[-1])-96)
print(f"{total:.2f}")
