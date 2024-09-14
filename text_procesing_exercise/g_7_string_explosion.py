words = input()
ecsplosion = 0
new_words = ""
for i in range(len(words)):
    if words[i] == ">":
        ecsplosion+=int(words[i+1])

    if ecsplosion == 0 or words[i] == ">":
        new_words+=words[i]
    else:
        ecsplosion-=1

print(new_words)