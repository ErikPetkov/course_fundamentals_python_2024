list = input().split(", ")
right = []
for i in range(len(list)):
    if int(list[i]) % 2 == 0:
        right.append(i)
print(right)