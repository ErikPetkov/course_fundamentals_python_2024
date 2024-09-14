key = int(input())
num = int(input())
for i in range(num):
    let = input()
    num_l = ord(let)
    num_l += key
    letr = chr(num_l)
    print(f"{letr}", end="")
