class Solution:
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        tar = []
        l = len(nums)
        nums = sorted(nums)
        i=0
        j=l-1
        mid = 1
        while i < j:
            if mid >= j:
                i += 1
                mid = i + 1
                continue
            num = nums[i]+nums[j]+nums[mid]
            if num > 0:
                j -= 1
            elif num < 0:
                mid += 1
            else:
                lists = [nums[i],nums[mid],nums[j]]
                if lists not in tar:
                    tar.append(lists)
                i += 1
                mid = i + 1
        return tar
arr = [0,0,0,0,0]#[-1,0,1,2,-1,-4]
s = Solution()
tar = s.threeSum(arr)
print(tar)