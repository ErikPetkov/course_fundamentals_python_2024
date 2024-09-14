iterations = int(input())
shearch = input()
al = []
sch = []
for _ in range(iterations):
    word = input()
    al.append(word)
    if shearch in word:
        sch.append(word)
print(al)
print(sch)