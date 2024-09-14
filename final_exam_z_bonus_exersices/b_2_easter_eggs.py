import re
text = input()
reg = r"[@#]+([a-z]{3,})[@#]+[^A-Za-z0-9]*?\/+(\d+)\/+"
matches = re.findall(reg, text)
for match in matches:
    color = match[0]
    amount = match[1]
    print(f"You found {amount} {color} eggs!")