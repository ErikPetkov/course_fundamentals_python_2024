def positive(base):
    return ", ".join([i for i in base if int(i) >= 0])
def negativ(base):
    return ", ".join([i for i in base if int(i) < 0])
def even(base):
    return ", ".join([i for i in base if int(i) % 2 == 0])
def odd(base):
    return ", ".join([i for i in base if int(i) % 2 == 1])


nums = input().split(", ")
print(f"Positive: {positive(nums)}")
print(f"Negative: {negativ(nums)}")
print(f"Even: {even(nums)}")
print(f"Odd: {odd(nums)}")
