def min_max_sun(list):
    int_list = []
    for i in list:
        int_list.append(int(i))
    max_num = max(int_list)
    min_num = min(int_list)
    sumed = sum(int_list)
    return max_num, min_num, sumed

listt = input().split()
num_max, num_min, total = min_max_sun(listt)
print(f"The minimum number is {num_min}")
print(f"The maximum number is {num_max}")
print(f"The sum number is: {total}")
