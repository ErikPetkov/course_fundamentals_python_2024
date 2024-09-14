n = int(input())
dict = {}
for i in range(n):
    word = input()
    sinonym = input()
    if word not in dict:
        dict[word] = []
    dict[word].append(sinonym)

for (key,value) in dict.items():
    print(f"{key}",end=" -")
    for val in value:
        if val == value[-1]:
            print(f" {val}")
        else:
            print(f" {val},",end="")


