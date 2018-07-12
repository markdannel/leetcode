nums = [1,2,3,4,5,6,7,8,9,2]

nums = sorted(nums)

i = 1
l = len(nums)

while i < l:
    if nums[i-1] == nums[i]:
        print("true",i)
        #return True
    i += 1
#return False

