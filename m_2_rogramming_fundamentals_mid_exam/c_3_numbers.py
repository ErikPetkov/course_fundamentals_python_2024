nums_st = input().split()
nums = [int(i) for i in nums_st]
av_num = sum(nums)/len(nums)
best_nums = []
count = 0
nums.sort()
nums = reversed(nums)
for n in nums:

    if av_num < n and count < 5:
        count += 1
        best_nums.append(n)
if best_nums == []:
    print("No")
best_nums.sort()
print(" ".join(str(g) for g in reversed(best_nums)))