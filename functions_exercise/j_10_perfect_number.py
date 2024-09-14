def isperfect(perdect_num):
    divisors = []
    for num in range(1,perdect_num):
        if perdect_num / num == perdect_num//num:
            divisors.append(num)
    if sum(divisors) == perdect_num:
        print("We have a perfect number!")
    else:
        print("It's not so perfect.")

perfect_number = int(input())
isperfect(perfect_number)