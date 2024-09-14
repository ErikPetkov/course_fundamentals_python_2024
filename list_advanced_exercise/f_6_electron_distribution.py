electrons = int(input())
n = 1
rings = []
while electrons > 0:
    ring = 2 * n ** 2
    if ring < electrons:
        electrons -= ring
        rings.append(ring)
    else:
        rings.append(electrons)
        electrons = 0
    n+=1
print("[", end="")
print(", ".join(str(i) for i in rings), end="]")