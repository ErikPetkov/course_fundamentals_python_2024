word = input()
strings = ""
nums = ""
chars = ""
for a in word:
    if a.isnumeric():
        nums += a
    elif a.isalpha():
        strings+=a
    else:
        chars+=a
print(nums)
print(strings)
print(chars)