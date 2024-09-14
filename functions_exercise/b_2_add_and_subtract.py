
def sum_numbers(num1, num2):
    return num2 + num1

def subtract(res, num3):
    return res - num3

first = int(input())
second = int(input())
third = int(input())
result = sum_numbers(first, second)
print(subtract(result, third))
