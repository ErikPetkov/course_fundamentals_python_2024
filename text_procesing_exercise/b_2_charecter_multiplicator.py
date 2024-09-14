tot_str = input().split()
total = 0
first_word = tot_str[0]
second_word = tot_str[1]
if len(first_word) > len(second_word):
    for index in range(len(second_word)):
        res = ord(first_word[index]) * ord(second_word[index])
        total+=res

    for i in range(len(second_word),len(first_word)):
        res = ord(first_word[i])
        total+=res
elif len(first_word) < len(second_word):
    for index in range(len(first_word)):
        res = ord(first_word[index]) * ord(second_word[index])
        total+=res
    for i in range(len(first_word), len(second_word)):
        res = ord(second_word[i])
        total += res
else:
    for index in range(len(second_word)):
        res = ord(first_word[index]) * ord(second_word[index])
        total+=res
print(total)


