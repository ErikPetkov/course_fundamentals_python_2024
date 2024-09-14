def factorial(num1, num2):
    num1_fact = 1
    num2_fact = 1
    for i in range(1, num1+1):
        num1_fact *= i
    for j in range(1, num2 + 1):
        num2_fact *= j
    return num1_fact/num2_fact

first = int(input())
second = int(input())
anser = factorial(first, second)
print(f"{anser:.2f}")