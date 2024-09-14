coffee = 0
while True:
    event = input()
    if event == "coding" or event == "dog" or event == "cat" or event == "movie":
        coffee += 1
    elif event == "CODING" or event == "DOG" or event == "CAT" or event == "MOVIE":
        coffee += 2
    elif event == "END":
        break
if coffee > 5:
    print("You need extra sleep")
else:
    print(coffee)