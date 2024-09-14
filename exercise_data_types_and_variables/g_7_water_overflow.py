num = int(input())
water = 255
ful = 0
for i in range(num):
    wat = int(input())
    if wat > water:
        print("Insufficient capacity!")
        continue
    ful += wat
    water-=wat
print(ful)
