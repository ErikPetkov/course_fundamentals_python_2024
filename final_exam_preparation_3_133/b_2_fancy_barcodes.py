import re

n = int(input())
goups = {}
for i in range(n):
    key = ""
    barcode = input()
    regex = r"@#+[A-Z][A-Za-z0-9]{4,}[A-Z]@#+"
    match = re.findall(regex,barcode)
    for a in barcode:
        if a.isdigit():
           key+=a
    if match != []:
        if key == "":
            print(f"Product group: 00")
        else:
            print(f"Product group: {key}")
    else:
        print("Invalid barcode")
