products = input().split()
needed = input().split()
dic = {}
for pr in range(0,len(products),2):
    key = products[pr]
    val = products[pr+1]
    dic[key] = int(val)

for need in needed:
    if need in dic:
        print(f"We have {dic[need]} of {need} left")
    else:
        print(f"Sorry, we don't have {need}")