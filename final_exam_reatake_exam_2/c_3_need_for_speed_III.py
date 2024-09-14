garage = {}
n = int(input())
for i in range(n):
    car_info = input().split("|")
    car = car_info[0]
    mileage = car_info[1]
    fuel = car_info[2]
    garage[car] = {
        "age":int(mileage), "fuel":int(fuel)
    }
comand = input().split(" : ")
while "Stop" not in comand:
    mission = comand[0]
    car = comand[1]
    if"Drive" == mission:
        distance = int(comand[2])
        fuel = int(comand[3])
        if garage[car]["fuel"] >= fuel:
            garage[car]["fuel"]-= fuel
            garage[car]["age"]+= distance
            print(f"{car} driven for {distance} kilometers. {fuel} liters of fuel consumed.")
            if garage[car]["age"] >= 100000:
                print(f"Time to sell the {car}!")
                del garage[car]

        else:
            print("Not enough fuel to make that ride")

    elif "Refuel" == mission:
        fuel = int(comand[2])
        old_fuel = garage[car]["fuel"]
        garage[car]["fuel"] += fuel
        if garage[car]["fuel"] > 75:
            garage[car]["fuel"] = 75
            print(f"{car} refueled with {75-old_fuel} liters")
        else:
            print(f"{car} refueled with {fuel} liters")
    elif "Revert" == mission:
        kilometers = int(comand[2])
        garage[car]["age"] -= kilometers

        if garage[car]["age"] < 10000:
            garage[car]["age"] = 10000
        else:
            print(f"{car} mileage decreased by {kilometers} kilometers")
    comand = input().split(" : ")

for car in garage.keys():

    print(f"{car} -> Mileage: {garage[car]["age"]} kms, Fuel in the tank: {garage[car]["fuel"]} lt.")
