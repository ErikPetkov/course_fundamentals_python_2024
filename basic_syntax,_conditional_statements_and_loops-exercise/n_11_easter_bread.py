budget = float(input())
kg_flour = float(input())
pack_eggs = kg_flour * 0.75
liter_milk = kg_flour * 1.25
cost = 0
bread = 0
colored_eggs = 0
buy = kg_flour + pack_eggs + liter_milk
milk = 0
while budget > buy:
    budget -= buy
    cost += buy
    bread += 1
    colored_eggs += 3
    if bread % 3 == 0:
        colored_eggs -= bread-2
    milk += 1
    if milk == 4:
        buy = kg_flour + pack_eggs + liter_milk
        milk = 0
    else:
        buy = kg_flour + pack_eggs
budget += milk * (liter_milk/4)
print(f"You made {bread} loaves of Easter bread!"
      f" Now you have {colored_eggs} eggs and {budget:.2f}BGN left.")
