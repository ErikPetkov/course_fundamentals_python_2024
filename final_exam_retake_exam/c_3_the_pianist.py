my_dict = {}
n = int(input())
for i in range(n):
    pieses = input().split("|")
    piece = pieses[0]
    composer = pieses[1]
    key = pieses[2]
    my_dict[piece] = {"composer":composer,
                      "key":key }

comand = input().split("|")
while "Stop" not in comand:
    mission = comand[0]
    piece = comand[1]
    if "Add" == mission:
        composer = comand[2]
        key = comand[3]
        if piece not in my_dict.keys():
            my_dict[piece] = {"composer": composer,
                              "key": key}
            print(f"{piece} by {composer} in {key} added to the collection!")
        else:
            print(f"{piece} is already in the collection!")
    elif "Remove" == mission:
        if piece in my_dict.keys():
            del my_dict[piece]
            print(f"Successfully removed {piece}!")
        else:
            print(f"Invalid operation! {piece} does not exist in the collection.")
    elif "ChangeKey" == mission:
        newkey = comand[2]
        if piece in my_dict.keys():
            my_dict[piece]["key"] = newkey
            print(f"Changed the key of {piece} to {newkey}!")
        else:
            print(f"Invalid operation! {piece} does not exist in the collection.")
    comand = input().split("|")

for ke in my_dict.keys():
    val1 = 0
    val2 = 0
    c = 1
    for value in my_dict[ke].values():
        if c == 1:
            val1 = value
            c = 0
        else:
            val2 = value
    print(f"{ke} -> Composer: {val1}, Key: {val2}")
    # print(f"{ke} -> Composer: {my_dict[ke]["composer"]}, Key: {my_dict[ke]["key"]}")
