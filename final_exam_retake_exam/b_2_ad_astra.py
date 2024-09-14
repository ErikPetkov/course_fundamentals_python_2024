import re
comands = input()
total_cal = 0
a = 0
# pattern = r";#[' 'a-zA-Z]+#[0-9]{2}/[0-9]{2}/[0-9]{2}#[0-9]+#|\|[' 'a-zA-Z]+\|\d{2}\|\d{2}\|\d{2}\|\d+\|;gm"
#p = #[" "a-zA-Z]+#[0-9]{2}\/[0-9]{2}\/[0-9]{2}#[0-9]+#|\|[" "a-zA-Z]+\|\d{2}\/\d{2}\/\d{2}\|\d+\|/gm
# pat = r";#[\sa-zA-Z]+#[0-9]{2}/[0-9]{2}/[0-9]{2}#[0-9]+#|[\sa-zA-Z]+\d{2}/\d{2}/\d{2}\d+;gm"
patt = r"([#|])([\sA-Za-z]+)\1(\d{2}\/\d{2}\/\d{2})\1(\d{1,4})\1"
matches = re.findall(patt, comands)
for match in matches:
    calories = int(match[3])
    total_cal+=calories

days = total_cal//2000
print(f"You have food to last you for: {days} days!")
for match in matches:
    item_name = match[1]
    expiration_date = match[2]
    calories = int(match[3])
    print(f"Item: {item_name}, Best before: {expiration_date}, Nutrition: {calories}")

