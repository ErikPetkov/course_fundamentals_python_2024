import re
n = int(input())
for _ in range(n):
    comand = input()
    reg = r"\|([A-Z]{4,})\|:#([A-Za-z]+\s[A-Za-z]+)#"
    match = re.findall(reg,comand)
    if match != []:
        match = match[0]
        boss = match[0]
        title = match[1]
        print(f"{boss}, The {title}")
        print(f">> Strength: {len(boss)}")
        print(f">> Armor: {len(title)}")
    else:
        print("Access denied!")
