energy = int(input())
distance = input()
won_batles = 0
while distance != "End of battle":
    distance = int(distance)

    won_batles += 1
    if energy <= distance:
        energy = abs(energy-distance)
        break

    energy -= distance
    if won_batles % 3 == 0:
        energy += won_batles

    distance = input()
if distance == "End of battle":
    print(f"Won battles: {won_batles}. Energy left: {energy}")
else:
    print(f"Not enough energy! Game ends with {won_batles} won battles and {energy} energy")
