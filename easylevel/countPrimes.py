import math
class Solution:
    def countPrimes(self, n):
        """
        :type n: int
        :rtype: int
        """
        # if n <= 2: return 0
        # flag = False
        # L = [2]
        # for i in range(3, n, 2):
            
        #     num = int(i**0.5)
        #     for j in L:
        #         if num < j:
        #             break
        #         if i % j == 0:
        #             flag = True
        #             break
        #     if not flag:
        #         L.append(i)
        #     flag = False
        # return len(L)
        m = int(n**0.5)
        arr = [1]*n
        arr[0] = arr[1] = 0
        l = len(arr)
        for i in range(2, m):
            if arr[i] != 0:
                for j in range(2*i, l, i):
                    arr[j] = 0
        return sum(arr)

s = Solution()
n = s.countPrimes(999983)
print(n)