def odd_even(string):
    sum_odd = 0
    sum_even = 0
    for i in string:
        i = int(i)
        if i == 0:
            continue
        elif i % 2 == 1:
            sum_odd += i
        elif i % 2 == 0:
            sum_even += i
    return sum_odd, sum_even

string = input()
su_odd, su_even = odd_even(string)
print(f"Odd sum = {su_odd}, Even sum = {su_even}")

