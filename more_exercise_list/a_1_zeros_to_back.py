my_list = input().split(", ")
for i in range(len(my_list)):
    if my_list[i] == "0":
        a = my_list[i]
        my_list.remove(str(0))
        my_list.append(a)
print("[", end="")
g = 0
for b in my_list:
    g += 1
    c = int(b)
    if b == my_list[-1] and g == len(my_list):
        print(c, end="]")
        break
    print(c, end=", ")
