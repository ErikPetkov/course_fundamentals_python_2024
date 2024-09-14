def inted(num):
    return int(num) * 2

def real(nun):
    return f"{float(nun) * 1.5:.2f}"

def stringed(num):
    return f"${num}$"

tipe = input()
number = input()
if tipe == "int":
    print(inted(number))
elif tipe == "real":
    print(real(number))
elif tipe == "string":
    print(stringed(number))