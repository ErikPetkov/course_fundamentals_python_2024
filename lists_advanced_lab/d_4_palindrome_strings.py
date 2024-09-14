palimd = []
palim = []
def palindro(list):
    for p in list:
        if p == "".join(reversed(p)) and p == shaerch:
            palimd.append(p)
        if p == "".join(reversed(p)):
            palim.append(p)
    return palimd, palim

list = input().split()
shaerch = input()
palindro(list)
print(f"{palim}")
print(f"Found palindrome {palimd.count(shaerch)} times")