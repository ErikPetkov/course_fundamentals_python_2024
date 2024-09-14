# number = int(input())
# for current_number in range(1, number + 1):
#     current_number_as_string = str(current_number)
#     digits_sum = 0
#     for digit in current_number_as_string:
#         digits_sum += int(digit)
#     is_special = False
#     if digits_sum == 5 or digits_sum == 7 or digits_sum == 11:
#         is_special = True
#     print(f"{current_number} -> {is_special}")
number = int(input())
for cirent_num in range(1, number+1):
    curent_num_str = str(cirent_num)
    dijit_sum = 0
    for dijit in curent_num_str:
        dijit_sum += int(dijit)
    is_special = False
    if dijit_sum == 5 or dijit_sum == 7 or dijit_sum == 11:
        is_special = True
    print(f"{cirent_num} -> {is_special}")
