comand = input()
products = {}
while "statistics" not in comand:

    key,value = comand.split(": ")
    if key not in products:
        products[key] = int(value)
    else:
        products[key] += int(value)
    comand = input()

print("Products in stock:")
tot_value = 0
for key,value in products.items():
    print(f"- {key}: {value}")
    tot_value+=value


print(f"Total Products: {len(products)}")
print(f"Total Quantity: {tot_value}")