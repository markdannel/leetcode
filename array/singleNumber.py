nums = [4,1,2,1,2,3,4]

nums = sorted(nums)
print(nums)
i = 1
l = len(nums)

if l < 2:
    return nums[0]
if nums[0] != nums[1]:
    print("first :",nums[0],nums)
    #return nums[0]

pren = nums[0]

while i < l:
    if nums[i-1] == nums[i]:
        pren = nums[i]
        i += 2
    else:
        if nums[i-1] == pren:
            i += 1
        else:
            print("diss:", nums[i-1], nums)
            #return nums[i-1]
print("last:", nums[l-1], nums)
#return nums[l-1]

