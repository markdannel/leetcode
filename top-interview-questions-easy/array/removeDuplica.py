class Solution:
    def removeDuplicates(self, nums) -> int:
        fir,sec=0,1
        l=len(nums)
        if l<2:
            return l
        while(sec <= l-1):
            if nums[fir]!=nums[sec]:
                fir+=1
                nums[fir]=nums[sec]
            sec+=1
        return fir+1

ll=[1,1,2,3,3,4]
s=Solution()
print(s.removeDuplicates(ll),ll)
