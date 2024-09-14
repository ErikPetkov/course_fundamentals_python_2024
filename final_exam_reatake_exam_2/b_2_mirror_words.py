import re
text = input()
my_dict = {}
reg = r"([@#])([A-Za-z]{3,})\1\1([A-Za-z]{3,})\1"
matches = re.findall(reg, text)
for match in matches:
    word_one = match[1]
    word_two = match[2]
    if word_one == word_two[::-1]:
        my_dict[word_one] = word_two
if len(matches) > 0:
    print(f"{len(matches)} word pairs found!")
else:
    print("No word pairs found!")
if len(my_dict.keys()) > 0:
    a = len(my_dict.keys())
    print("The mirror words are:")
    cey = 1
    for key, value in my_dict.items():
        if cey == 1:
            print(f"{key} <=> {value}",end= "")
            cey = 0
        else:
            print(f", {key} <=> {value}",end= "")
else:
    print("No mirror words!")
