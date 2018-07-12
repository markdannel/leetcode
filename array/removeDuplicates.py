nums = [1,1,2]#[0,0,1,1,1,2,2,3,3,4]

i = 1

while i < len(nums):
    if nums[i] == nums[i-1]:
        nums.pop(i)
        i -= 1
    i += 1
print(nums)

'''
nums[:] = sorted(list(set(nums)))
return len(set(nums))
'''