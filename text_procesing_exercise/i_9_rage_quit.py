enterence = input()
word = ""
output = ""
sumv = ""
for char in enterence:
    if not char.isdigit():
        word+=char
        if char not in sumv:
            sumv+=char.lower()
    else:
        num = int(char)
        for i in range(num):
            output+= word.upper()
        word = ""
print(f"Unique symbols used: {len(set(sumv))}")
print(output)

# text = input()
# rage_message = ""
# repetitions = ""
# sub_string = ""
# for index in range(len(text)):
#     if not text[index].isdigit(): # non-numeric symbol
#         sub_string += text[index].upper()
#     else: # number of repetitions
#         for next_symbols in range(index, len(text)):
#             if not text[next_symbols].isdigit():
#                 break
#             repetitions += text[next_symbols]
#         rage_message += sub_string * int(repetitions)
#         repetitions = ""
#         sub_string = ""
# print(f"Unique symbols used: {len(set(rage_message))}")
# print(rage_message)