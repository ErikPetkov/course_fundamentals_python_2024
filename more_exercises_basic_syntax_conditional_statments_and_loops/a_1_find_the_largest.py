num = int(input())
list = []
list += num
list.sort()
while len(list) != 0:
    list = str(list)
    big_num = list[-1]
    list.remove(-1)
print(big_num)
