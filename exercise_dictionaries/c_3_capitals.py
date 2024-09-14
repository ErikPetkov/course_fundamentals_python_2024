country = input().split(", ")
city = input().split(", ")
dict = dict(zip(country,city))

for key in dict.keys():
    print(f"{key} -> {dict[key]}")