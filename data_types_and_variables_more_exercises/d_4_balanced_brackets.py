lines = int(input())
opening = 0
closing = 0
for _ in range(lines):
    random_str = input()
    if "(" in random_str:
        opening += 1
    elif ")" in random_str:
        closing += 1
if opening == closing:
    print("BALANCED")
else:
    print("UNBALANCED")