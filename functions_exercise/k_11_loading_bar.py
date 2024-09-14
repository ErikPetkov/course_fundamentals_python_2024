def loading(percent):
    n = percent//10
    if n == 10:
        print("100% Complete!")
    else:
        print(percent, end="% ")
    print("[", end="")
    for i in range(n):
        print("%", end="")
    for _ in range(n, 10):
        print(".", end="")
    print("]")
    if n != 10:
        print("Still loading...")

percen = int(input())
loading(percen)