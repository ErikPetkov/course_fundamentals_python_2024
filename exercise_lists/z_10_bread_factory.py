day = input().split("|")
energy = 100
money = 100
closed = True
for things in day:
    event, number = things.split("-")
    number = int(number)
    if event == "rest":
        energy += number
        if energy > 100:
            energy = 100
            number = 0
        print(f"You gained {number} energy.")
        print(f"Current energy: {energy}.")
    elif event == "order":
        if energy >= 30:
            money += number
            energy -= 30
            print(f"You earned {number} coins.")
        else:
            energy += 50
            print("You had to rest!")
    else:
        if money >= number:
            money -= number
            print(f"You bought {event}.")
        else:
            print(f"Closed! Cannot afford {event}.")
            closed = False
            break
if closed:
    print("Day completed!")
    print(f"Coins: {money}")
    print(f"Energy: {energy}")
