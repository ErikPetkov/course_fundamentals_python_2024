nums = input().split(", ")
maxed = max([int(n) for n in nums])
right_num = maxed // 10 + 1
group = [[] for _ in range(right_num)]
for i in nums:
    i = int(i)
    if i//10 == i /10:
        index = i // 10-1
    else:
        index = i // 10
    group[index].append(i)

# print(group)
for b in range(right_num):
    if maxed //10 == maxed / 10:
        if b == right_num-1:
            pass
        else:
            print(f"Group of {(b + 1) * 10}'s: [{', '.join([str(c) for c in group[b]])}]")
    else:
        print(f"Group of {(b+1)*10}'s: [{', '.join([str(c) for c in group[b]])}]")