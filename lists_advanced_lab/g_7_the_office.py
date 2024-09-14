hapines_list = input().split()
happy = int(input())
moded = []
hapines_int = map(lambda  x: int(x) * happy, hapines_list)
filtered = list(filter(lambda a: int(a) * happy, hapines_list))
if len(filtered >= len(hapines_list) / 2):
    print(f"Score: {len(filtered)}/{len(hapines_list)}. Employees are happy!")
else:
    print(f"Score: {len(filtered)}/{len(hapines_list)}. Employees are not happy!")