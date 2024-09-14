def filter(list_nums):
    even_list = []
    for i in list_nums:
        i = int(i)
        if i%2 == 0:
            even_list.append(i)
    return even_list
list_num = input().split()
print(filter(list_num))