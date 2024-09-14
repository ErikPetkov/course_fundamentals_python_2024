from re import *
lokation = input()
regex = r"\=[A-Z][a-zA-Z][a-zA-Z]+\=|\/[A-Z][a-zA-Z]+\/"
match = findall(regex, lokation)
valid = []
points = 0

for des in match:
    des = str(des).replace("=","")
    des = str(des).replace("/","")
    points += len(des)
    valid.append(des)
# points = len(match)
print("Destinations: "+", ".join(valid))
print(f"Travel Points: {points}")