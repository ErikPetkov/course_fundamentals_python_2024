info = input().split(":")
data = []
cus = ""
curse = 0
while True:
    if len(info) == 1:
        curse = str(info[0])
        break
    data.append(info)
    info = input().split(":")
for a in curse:
    if a != "_":
        cus += a
    else:
        cus+=" "
for student in data:

    if cus == student[-1]:
        print(f"{student[0]} - {student[1]}")