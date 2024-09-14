buy = int(input())
day_to_crismas = int(input())
ornament_set = 2
tree_skirt = 5
tree_garlnd = 3
tree_lights = 15
cost = 0
bu = buy
spirit = 0
for curent_day in range(1, day_to_crismas+1):
    if curent_day % 11 == 0:
        buy += 2
    if curent_day % 2 == 0:
        cost += buy * ornament_set
        spirit += 5
    if curent_day % 3 == 0:
        cost += (tree_skirt + tree_garlnd) * buy
        spirit += 13
    if curent_day % 5 == 0:
        cost += 15 * buy
        spirit += 17
        if curent_day % 3 == 0:
            spirit += 30
    if curent_day % 10 == 0:
        spirit -= 20
        cost += (tree_skirt + tree_lights + tree_garlnd)
if day_to_crismas % 10 == 0:
    spirit -= 30
print(f"Total cost: {cost}")
print(f"Total spirit: {spirit}")


