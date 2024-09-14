money = input().split(", ")
money_as_int = []
num_of_beggars = int(input())
for mone in money:
    money_as_int.append(int(mone))
beggars_get = []
start = 0
for begger in range(num_of_beggars):
    beggar_gets = []
    for i in range(start, len(money_as_int), num_of_beggars):
        beggar_gets += money_as_int[i]
    beggars_get.append(beggar_gets)
    start += 1
print(beggars_get)
