from math import sqrt, floor

def cordinat(x, xn, y, yn):
    return sqrt((x-xn)**2 + (y-yn)**2)

def cordinad(x, y):
    return sqrt((x)**2 + (y)**2)

x1 = float(input())
y1 = float(input())
x2 = float(input())
y2 = float(input())
x3 = float(input())
y3 = float(input())
x4 = float(input())
y4 = float(input())
first_rwo = False

cord1 = cordinad(x1, y1)
cord2 = cordinad(x2, y2)
cord3 = cordinad(x3, y3)
cord4 = cordinad(x4, y4)
if cord1 == min(cord1, cord2, cord3, cord4) or cord2 == min(cord1, cord2, cord3, cord4):
    line1 = cordinat(x1, y1, x2, y2)
    first_rwo = True
    line2 = cordinat(x3, y3, x4, y4)
elif cord3 == min(cord1, cord2, cord3, cord4) or cord4 == min(cord1, cord2, cord3, cord4):
    line1 = cordinat(x1, y1, x2, y2)
    line2 = cordinat(x3, y3, x4, y4)

if first_rwo:
    if line1 >= line2:
        print(f"({floor(x2)}, {floor(y2)})({floor(x1)}, {floor(y1)})")
    elif line1 < line2:
        print(f"({floor(x4)}, {floor(y4)})({floor(x3)}, {floor(y3)})")
elif not first_rwo:
    if line1 > line2:
        print(f"({floor(x2)}, {floor(y2)})({floor(x1)}, {floor(y1)})")
    elif line1 <= line2:
        print(f"({floor(x4)}, {floor(y4)})({floor(x3)}, {floor(y3)})")

