br_people = int(input())
lift_st = input().split()
lift = [int(i) for i in lift_st]
have_people = True
iteration = 0
for cabin in lift:
    while cabin < 4:
        if br_people <= 0:
            have_people = False
            break
        cabin += 1
        br_people -= 1
    lift.remove(lift[iteration])
    lift.insert(iteration, cabin)
    iteration += 1

    if not have_people:
        break
if not have_people:
    print("The lift has empty spots!")
    print(f"{' '.join(str(a) for a in lift)}")
elif br_people == 0:
    print(' '.join(str(b) for b in lift))
else:
    print(f"There isn't enough space! {br_people} people in a queue!")
    print(f"{' '.join(str(v) for v in lift)}")
