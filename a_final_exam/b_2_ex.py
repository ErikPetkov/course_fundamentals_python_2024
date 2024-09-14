# n = int(input())
# import re
#
# for i in range(n):
#     password = input()
#     # regex = r"^([^><\w]+)>[0-9]+\|[a-z]+\|[A-Z]+\|\W+[^><]<\1$"
#     # regex = r"^([^><]+)>[0-9]+\|[a-z]+\|[A-Z]+\|\W+[^><]<\1$"
#     regex = r'^([^\s<>]+)>(\d{3}|[a-z]{3}|[A-Z]{3}|[^<>]{3})<\1$'
#
#     match = re.findall(regex,password)
#     if match == []:
#         print("Try another password!")
#     else:
#         password = password.split(">")
#         password = password[1]
#         password = password.split("<")
#         password = password[0]
#         password = password.split("|")
#         p = ""
#         for i in password:
#             p += i
#         encript_pas = p
#         print(f"Password: {encript_pas}")
import re

pattern = r'^([^\s<>]+)>(\d{3}\|[a-z]{3}\|[A-Z]{3}\|[^<>]{3})<\1$'
num = int(input())
for i in range(num):
    password = input()
    lst = re.findall(pattern, password)
    if not lst:

        print("Try another password!")
    else:
        lst = lst[0][1].split("|")
        print(f"Password: {''.join(lst)}")