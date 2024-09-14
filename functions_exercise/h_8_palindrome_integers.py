def palindrom(list):
    result = ""
    for i in list:
        if i == i[::-1]:
            result += 'True\n'
        else:
            result += 'False\n'
    print(result)

pal = input().split(", ")
palindrom(pal)


