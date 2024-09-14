def sorted(list):
    list_int = []
    for i in list:
        list_int.append(int(i))
    list_int.sort()
    return list_int

listt = input().split()
print(sorted(listt))

