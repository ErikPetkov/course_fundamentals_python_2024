import re
numbers = input()
regex = r"\+359 2 \d{3} \d{4}|\+359-2-\d{3}-\d{4}"
matches = re.findall(regex, numbers)
print(", ".join(set(matches)))