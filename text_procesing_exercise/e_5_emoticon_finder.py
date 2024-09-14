words = input()
for i in range(len(words)):
    if words[i] == ":":
        print(f"{words[i]}{words[i+1]}")