words = input()
decripted = ""
for char in words:
    decripted+= chr(ord(char)+3)
print(decripted)