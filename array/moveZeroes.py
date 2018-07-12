nums = [0,0,1]

l = len(nums)
i = 0
j = 0

while j < l:
    if nums[i] == 0:
        nums.pop(i)
        nums.append(0)
    else:
        i += 1
    j += 1
print(nums)

