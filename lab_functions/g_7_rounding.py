
def rounding(lists):
    for a in lists:
        rounded.append(round(float(a)))
    return rounded
rounded = []
list = input().split()
round_list = rounding(list)
print(round_list)