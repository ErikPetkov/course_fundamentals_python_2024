import math
def cordinat(x, y):
    return math.sqrt((x)**2 + (y)**2)

x1 = float(input())
y1 = float(input())
x2 = float(input())
y2 = float(input())
cord1 = cordinat(x1, y1)
cord2 = cordinat(x2, y2)
if cord1 < cord2:
    print(f"({math.floor(x1)}, {math.floor(y1)})")
elif cord1 > cord2:
    print(f"({math.floor(x2)}, {math.floor(y2)})")
elif cord1 == cord2:
    print(f"({math.floor(x1)}, {math.floor(y1)})")
