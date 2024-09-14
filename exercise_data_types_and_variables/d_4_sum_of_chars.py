nums = int(input())
tot = 0
for i in range(nums):
    aski = input()
    tot += ord(aski)
print(f"The sum equals: {tot}")