num1 = int(input())
num2 = int(input())
for i in range(num2, 0, -1):
    if i % num1 == 0:
        print(i)
        break
