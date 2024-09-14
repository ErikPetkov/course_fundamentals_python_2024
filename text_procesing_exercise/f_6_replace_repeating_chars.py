word = input()
last_char = ""
last = ""
for char in word:
    if char != last_char:
        last+=char
        last_char = char
print(last)