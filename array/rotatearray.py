nums = [1,2,3,4,5,6]#[1,2,3,4,5,6,7,8,9,10]
k = 4

l = len(nums)
#if l < 2: return nums
#if k%l == 0: return nums
k = (l+k)%l
i = 0

while i < k:
    temp = nums.pop()
    nums.insert(0, temp)
    i += 1

# ff = l%k
# t = nums[l-1]
# i = 0
# add=0

# if ff > 0:
#     while i < l:
#         nums[l-1-add] = nums[(2*l-1-add-k)%l]
#         add += k
#         add %= l
#         i += 1
#     nums[k-1] = t

# else:
#     while i < k:
#         t = nums[(2*l-1-i)%l]
#         j = 0
#         while j < l/k:
#             nums[l-1-i-add] = nums[(2*l-1-add-k-i)%l]
#             add += k
#             add %= l
#             j += 1
#         nums[k-1-i] = t
#         i += 1


print(nums)