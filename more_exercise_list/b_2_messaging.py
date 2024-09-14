list_nums = input().split()
strings = input()
right_str = ""
print_str = ""
nums = 0

for l in strings:
    if l == " ":
        continue
    right_str += l



for i in range(len(list_nums)):

    for a in list_nums[i]:
       nums += int(a)

    while True:
        if nums > len(right_str):
            nums -= len(right_str)
        else:
            break

    for b in range(len(right_str)):
        if b == nums:
            print_str += right_str[b]
            right_str = right_str.replace(right_str[b], "")
print(print_str)



