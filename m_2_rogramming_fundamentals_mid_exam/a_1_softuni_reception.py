first_employ_per_hour = int(input())
second_employ_per_hour = int(input())
third_employ_per_hour = int(input())
students = int(input())
hours = 0
breaks = 0
help_per_hour = first_employ_per_hour + second_employ_per_hour+third_employ_per_hour

while help_per_hour < students:
    hours += 1
    students -= help_per_hour
    if hours % 3 == 0:
        breaks += 1
if students != 0:
    hours += 1
time = hours + breaks
print(f"Time needed: {time}h.")
