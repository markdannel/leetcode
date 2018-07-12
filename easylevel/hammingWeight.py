class Solution:
    def hammingWeight(self, n):
        count = 0
        arr = []
        while n:
            if n%2 == 1:
                count += 1
                arr.append(1)
            else:
                arr.append(0)
            n = n//2
        print(count, arr)
s = Solution()
s.hammingWeight(257)