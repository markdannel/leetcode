class Solution:
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l = len(nums)
        if nums == []:
            return 0
        if l == 1:
            return nums[0]
        dp = [0]*l
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])
        for i in range(2, l):
            dp[i] = max(dp[i-1], dp[i-2]+nums[i])
        return dp[l-1]
s = Solution()
n = s.rob([1,3,2,1,4])
print(n)