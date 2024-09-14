str_1 = input()
str_2 = input()
last_print = str_1
for i in range(len(str_1)):
    left_part = str_2[:i+1]
    right_part = str_1[i+1:]
    new_str = left_part + right_part
    if new_str != last_print:
        print(new_str)
        last_print = new_str
