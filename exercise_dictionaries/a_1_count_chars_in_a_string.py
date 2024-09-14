code = input().split(" ")
dict = {}
for word in code:
    for w in word:
        if w not in dict:
            dict[w] = 0
        dict[w]+=1

for (key, value) in dict.items():
    print(f"{key} -> {value}")