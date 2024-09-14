info = input().split("|")
budjet = int(input())
profit = []
gaved = 0
for sell in info:
    typ, price = sell.split("->")
    price = float(price)
    if typ == "Clothes":
        if price <= 50:
            if budjet < price:
                break
            budjet -= price
            gaved += price *1.4
            erned = price * 1.4
        else:
            continue
    elif typ == "Shoes":
        if price <= 35:
            if budjet < price:
                break
            budjet -= price
            gaved += price *1.4
            erned = price * 1.4
        else:
            continue
    elif typ == "Accessories":
        if price <= 20.5:
            if budjet < price:
                break
            budjet -= price
            gaved += price *1.4
            erned = price * 1.4
        else:
            continue
    else:
        continue
    profit.append(f"{erned:.2f}")
a = 0
for n in profit:
    a += float(n)
woned = a - gaved
for g in profit:
    print(float(g),end=" ")
print()
print(f"Profit: {woned:.2f}")
if budjet+a >= 150:
    print("Hello, France!")
else:
    print("Not enough money.")