comand = input()
price_with_out_taxes = 0
while True:
    if comand == "special":
        break
    if comand == "regular":
        break
    if float(comand) < 0:
        print("Invalid price!")
    else:
        price_with_out_taxes += float(comand)
    comand = input()
price_with_taxes = price_with_out_taxes * 1.2
if comand == "special":
    price_with_taxes *= 0.9
if price_with_taxes == 0:
    print("Invalid order!")
else:
    print("Congratulations you've just bought a new computer! ")
    print(f"Price without taxes: {price_with_out_taxes:.2f}$")
    taxes = price_with_out_taxes * 0.2
    print(f"Taxes: {taxes:.2f}$")
    print("-----------")
    print(f"Total price: {price_with_taxes:.2f}$")