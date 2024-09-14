n = int(input())
plant_data = {}
for i in range(n):
    date = input().split("<->")
    key = date[0]
    reality = date[1]
    plant_data[key] = {}
    plant_data[key][reality] = 0

comand = input()
while "Exhibition" != comand:
    if "Rate" in comand:
        comand = comand.split(": ")
        comand = comand[1].split(" - ")
        plant = comand[0]
        rating = comand[1]
        reality = list(plant_data[plant].keys())
        if plant_data[plant][reality[0]] != 0:
            ratin = plant_data[plant][reality[0]]
            av_rating = (int(rating)+int(ratin))/2
            plant_data[plant][reality[0]] = str(av_rating)
        else:
            plant_data[plant][reality[0]] = rating
    elif "Update: " in comand:
        comand = comand.split(": ")
        comand = comand[1].split(" - ")
        plant = comand[0]
        new_riarity = comand[1]
        old_riality = list(plant_data[plant].keys())
        plant_data[plant][new_riarity] = plant_data[plant][old_riality[0]]
        del plant_data[plant][old_riality[0]]

    elif "Reset: " in comand:
        comand = comand.split(": ")
        plant = comand[1]
        reality = list(plant_data[plant].keys())
        plant_data[plant][reality[0]] = 0
    else:
        print("error")
    comand = input()

print("Plants for the exhibition:")
for key in plant_data.keys():
    plant_name = key
    rarity = list(plant_data[key].keys())
    rarit = int(rarity[0])
    average_rating = float(plant_data[key][rarity[0]])
    print(f"- {plant_name}; Rarity: {rarit}; Rating: {average_rating:.2f}")