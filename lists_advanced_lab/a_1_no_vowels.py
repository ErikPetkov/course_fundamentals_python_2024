word = input()
made = [x for x in word if x.lower() not in "a o u e i"]
vowel = ""
for p in made:
    vowel += p
print(vowel)
