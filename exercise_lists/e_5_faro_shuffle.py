cards = input().split(" ")
shuffles = int(input())
for shuffle in range(shuffles):
    middle = len(cards)//2
    left = cards[:middle]
    right = cards[middle:]
    dec_after_shuffling = []
    for card_index in range(len(left)):
        dec_after_shuffling.append(left[card_index])
        dec_after_shuffling.append(right[card_index])
    cards = dec_after_shuffling
print(cards)
