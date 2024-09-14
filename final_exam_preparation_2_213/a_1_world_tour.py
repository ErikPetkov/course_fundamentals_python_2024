stops_map = input()
comand = input().split(":")

while "Travel" not in comand:
    com1 = comand[1]
    com2 = comand[2]
    if "Add Stop" in comand:
        com1 = int(com1)
        if com1 < len(stops_map):

            stops_map = stops_map[:com1]+com2+stops_map[com1:]

    elif "Remove Stop" in comand:
        com1 = int(com1)
        com2 = int(com2)
        stops_map = stops_map[:com1]+ stops_map[com2+1:]

    elif "Switch" in comand:
        stops_map = stops_map.replace(com1,com2)

    print(stops_map)
    comand = input().split(":")
print(f"Ready for world tour! Planned stops: {stops_map}")