grup_size = int(input())
days = int(input())
coins = 0
for day in range(1, days+1):
    if day % 10 == 0:
        grup_size -= 2
    if day % 15 == 0:
        grup_size += 5
    coins += 50
    coins -= grup_size*2
    if day % 3 == 0:
        coins -= grup_size*3
    if day % 5 == 0:
        coins += 20*grup_size
        if day % 3 == 0:
            coins -= 2*grup_size
coins_per_person = coins//grup_size
print(f"{grup_size} companions received {coins_per_person} coins each.")