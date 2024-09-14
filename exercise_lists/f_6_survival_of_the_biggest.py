nums = input().split(" ")
remove = int(input())
nums_int = []
for n in nums:
    nums_int.append(int(n))
for i in range(1, remove + 1):
    nums_int.remove(min(nums_int))
print(*nums_int, sep=", ")

# number_list = input().split()
# count_of_remove = int(input())
#
# number_list_int = []
#
# for items in number_list:
#     number_list_int.append(int(items))
#
# for smallest in range(count_of_remove):
#     number_list_int.remove(min(number_list_int))
#
# print(*number_list_int, sep=', ')