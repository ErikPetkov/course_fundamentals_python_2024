orders = int(input())
total_price = 0
for i in range(orders):
    price_per_capsule = float(input())
    days = int(input())
    capsulesper_day = int(input())
    if price_per_capsule < 0.01 or price_per_capsule > 100:
        continue
    elif days < 1 or days > 31:
        continue
    elif capsulesper_day < 1 or capsulesper_day > 2000:
        continue
    price = price_per_capsule * days * capsulesper_day
    print(f"The price for the coffee is: ${price:.2f}")
    total_price += price
print(f"Total: ${total_price:.2f}")
