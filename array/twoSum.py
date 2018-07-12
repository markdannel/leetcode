nums = [3,2,4]
target = 6

def find(one, two):
    i = 0
    while i < l:
        if nums[i] == one or nums[i] == two:
            res.append(i)
        i += 1
    return

l = len(nums)

sort = sorted(nums)

res = []
i = 0
j = l-1

while i < l:
    if (sort[i] + sort[j]) > target:
        j -= 1
    elif (sort[i] + sort[j]) < target:
        i += 1
    else:
        find(sort[i], sort[j])
        break

res = sorted(res)
print(res)

