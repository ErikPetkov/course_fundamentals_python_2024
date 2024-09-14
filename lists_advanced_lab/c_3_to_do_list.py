notes = [0] * 10
while True:
    comand = input()
    if comand == "End":
        break
    tolkens = comand.split("-")
    priority = int(tolkens[0]) - 1
    note = tolkens[1]
    notes.pop(priority)
    notes.insert(priority, note)
no = []
for a in notes:
    if a == 0:
        continue
    no += a
print(no)
