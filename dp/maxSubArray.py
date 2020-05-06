def maxSubArray():
    nums = []
    maxp = nums[0] or 0
    nc = 0
    for i in nums:
        nc += i
        maxp = max(maxp, nc)
        if nc < 0:
            nc = 0
    return maxp
print(maxSubArray())
