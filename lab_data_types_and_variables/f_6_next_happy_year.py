year = int(input())

while True:
    year += 1
    happy_year = True
    year_str = ""
    for digit in str(year):
        if digit in year_str:
            happy_year = False
            break
        year_str += digit
    if happy_year:
        break
print(year)
