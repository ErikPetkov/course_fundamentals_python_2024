
def calculate(thing, num):
    if thing == "coffee":
        return 1.5 * num
    elif thing == "coke":
        return 1.4 * num
    elif thing == "water":
        return 1 * num
    elif thing == "snacks":
        return 2 * num

product = input()
br = int(input())
res = calculate(product, br)
print(f"{res:.2f}")