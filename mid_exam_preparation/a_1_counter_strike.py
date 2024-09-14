def cheat(a):
    while True:
        if a in board:
            a += 1
        else:
            i = len(board) // 2
            board.insert(i, a)
            board.insert(i, a)
            return


board = input().split()
lied = False
turns = 0
coman = input().split()
while True:
    if board == []:
        break
    if "end" in coman:
        break
    turns += 1
    piced1, piced2 = coman
    piced1 = int(piced1)
    piced2 = int(piced2)
    if piced1 < 0 or piced1 > len(board):
        a = f"-{turns}a"
        cheat(a)
        print("Invalid input! Adding additional elements to the board")
    elif piced2 < 0 or piced2 > len(board):
        a = f"-{turns}a"
        cheat(a)
        print("Invalid input! Adding additional elements to the board")
    elif board[piced1] == board[piced2]:
        print(f"Congrats! You have found matching elements - {board[piced1]}!")
        l,m = board[piced1],board[piced2]
        board.remove(l), board.remove(m)
    else:
        print("Try again!")
    coman = input().split()
if "end" in coman:
    print("Sorry you lose :(")
    print(f"{' '.join(z for z in board)}")
else:
    print(f"You have won in {turns} turns!")