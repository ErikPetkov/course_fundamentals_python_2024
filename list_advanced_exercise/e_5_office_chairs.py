rooms = int(input())
free_chairs = 0
error = False
for i in range(1, rooms+1):
    chairs, people = input().split()
    people = int(people)
    if len(chairs) >= people:
        free_chairs += abs(len(chairs) - people)
    else:
        print(f"{len(chairs)- people} more chairs needed in room {i}")
        error = True
if free_chairs >= 0:
    print(f"Game On, {free_chairs} free chairs left")