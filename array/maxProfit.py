class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        l = len(prices)
        if l <= 1: return 0
        maxp = minp = prices[0]
        flag = -1
        sum = 0
        for i in range(1, l):
            if prices[i] > prices[i-1]:
                if flag == 0:
                    minp = prices[i-1]
                flag = 1
            elif prices[i] < prices[i-1]:
                #maxp = prices[i-1]
                if flag == 1:
                    sum += prices[i-1] - minp
                    minp = 0
                flag = 0
        if minp != 0 and flag != 0:
            sum += prices[l-1] - minp
        return sum
arr = range(9999,1,-1)
s = Solution()
n = s.maxProfit(arr)
print(n)

# prices = range(9999,1,-1)#[7,1,5,3,6,4]#[4,7,3,2,1,2]#[1,4,2,7]

# l = len(prices)
# maxp = [0] * l
# i = 0
# r = 0
# prer = 0

# while i < l:
#     j = i + 1
#     while j < l:
#         prer = r
#         r = prices[j] - prices[i]
#         if prer < 0 and r < 0: break
#         if r > 0 and (i-1) > 0:
#             maxp[j] = max(maxp[j], maxp[j-1], r+max(*maxp[:i],0))
#         else:
#             maxp[j] = max(maxp[j], maxp[j-1], r)
#         j += 1
#     i += 1
# print(maxp, maxp[l-1], max(maxp))
