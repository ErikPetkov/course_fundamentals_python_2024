coman = input()
my_dict = {}
count_all_food_quantity = 0
while coman != "Complete":
    comand = coman.split()
    quatity = int(comand[1])
    food = comand[2]
    if "Receive" in comand:
        if quatity > 0:
            if food not in my_dict:
                my_dict[food] = 0
            my_dict[food] += quatity
    elif "Sell" in comand:
        if food not in my_dict.keys():
            print(f"You do not have any {food}.")
        elif my_dict[food] < quatity:
            sold_quantity = my_dict[food]
            count_all_food_quantity += sold_quantity
            del my_dict[food]
            print(f"There aren't enough {food}. You sold the last {sold_quantity} of them.")
        else:
            my_dict[food]-=quatity
            print(f"You sold {quatity} {food}.")
            count_all_food_quantity += quatity
            if my_dict[food] == 0:
                del my_dict[food]
    coman = input()

for key,value in my_dict.items():
    print(key+": "+str(value))
print(f"All sold: {count_all_food_quantity} goods")