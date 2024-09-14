def numers(n1, n2, n3):
    if n1 == 0:
        return "zero"
    if n2 == 0:
        return"zero"
    if n3 == 0:
        return "zero"
    if n1 > 0:
        if n2 > 0:
            if n3 > 0:
                return "positive"
            if n3 < 0:
                return "negative"
        if n2 < 0:
            if n3 > 0:
                return "negative"
            if n3 < 0:
                return "positive"
    if n1 < 0:
        if n2 > 0:
            if n3 > 0:
                return "negative"
            if n3 < 0:
                return "positive"
        if n2 < 0:
            if n3 > 0:
                return "positive"
            if n3 < 0:
                return "negative"

num1 = int(input())
num2 = int(input())
num3 = int(input())
print(numers(num1, num2, num3))
