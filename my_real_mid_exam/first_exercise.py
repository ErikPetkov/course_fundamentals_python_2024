from math import ceil
budget = float(input())
students = int(input())
price_flour = float(input())
price_egg = float(input())
price_of_apron = float(input())

free_flour = students//5
tot_eggs = students*10*price_egg
tot_flour = price_flour * (students-free_flour)
tot_apron = price_of_apron * (ceil(students*1.2))
cost = tot_eggs + tot_flour + tot_apron
diff = abs(budget-cost)
if cost <= budget:
    print(f"Items purchased for {cost:.2f}$.")
else:
    print(f"{diff:.2f}$ more needed.")
