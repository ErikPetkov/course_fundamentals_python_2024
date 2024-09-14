number = int(input())

special = []
num = []
for i in range(number):
    nums = int(input())
    num.append(nums)
comand = input()
for i in num:
    if comand == "even" and i % 2 == 0:
        special.append(i)
    elif comand == "odd" and i % 2 == 1:
        special.append(i)
    elif comand == "negative" and i < 0:
        special.append(i)
    elif comand == "positive" and i >= 0:
        special.append(i)
print(special)
