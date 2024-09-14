code = input().split()
craked = []
for text in code:


    for i in range(65, 90):
        text = text.replace(str(i), chr(i))

    for i in range(97, 122):
        text = text.replace(str(i), chr(i))

    tex2 = text[1]
    tex = text[-1]
    text.replace(tex2, tex)
    craked.append(text)
print(" ".join(s for s in craked))
