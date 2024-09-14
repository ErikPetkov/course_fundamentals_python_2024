search = input().split(", ")
words = input().split(", ")
found = []
for word in search:
    for wor in words:
        if word in wor:
            found.append(word)
            break
print(found)