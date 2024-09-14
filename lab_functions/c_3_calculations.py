
def calcolate(first, second, operation):
    if operation == "add":
        return first + second
    elif operation == "subtract":
        return first - second
    elif operation == "multiply":
        return first * second
    elif operation == "divide":
        return first // second

input_operation = input()
first_num = int(input())
second_num = int(input())
res = calcolate(first_num, second_num, input_operation)
print(res)