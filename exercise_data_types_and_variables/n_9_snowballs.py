num_snow_balls = int(input())
best_weight = 0
best_time = 0
best_quality = 0
best_value = 0
for ball in range(num_snow_balls):
    weight = int(input())
    time_n = int(input())
    quality = int(input())
    value = (weight/time_n) ** quality
    if value > best_value:
        best_weight = weight
        best_time = time_n
        best_value = int(value)
        best_quality = quality
print(f"{best_weight} : {best_time} = {best_value} ({best_quality})")
