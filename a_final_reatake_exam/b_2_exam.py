import re
my_dict = ()
string = input().split("!")
for i, l in enumerate(0,len(string),2):
    my_dict[i] = l
ref = r"([#$%*&])([A-Za-z]+)\1=([\d]+)!"
match = re.findall(ref, string)
if match != {}:
    print("Nothing found!")
else:
    if list(match)==0:
        pass