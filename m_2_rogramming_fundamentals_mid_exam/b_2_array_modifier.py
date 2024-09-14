def swapPositions(arr, pos1, pos2):
    arr[pos1], arr[pos2] = arr[pos2], arr[pos1]
    return arr
arrey_st = input().split()
arrey = [int(a) for a in arrey_st]
comand = input()
while comand != "end":
    if "swap" in comand:
        in1 = comand[1]
        in2 = comand[2]
        swapPositions(arrey, in1, in2)
    elif "multiply" in comand:
        in1 = comand[1]
        in2 = comand[2]
        arrey[in1] += arrey[in2]
    elif "decrease" in comand:
        arrey = [ i-1 for i in arrey]

print(", ".join([b for b in arrey]))