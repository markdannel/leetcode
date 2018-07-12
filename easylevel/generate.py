class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        arr = [[1],[1,1]]
        for i in range(2, numRows):
            arr.append([1])
            for j in range(1, i):
                arr[i].append(arr[i-1][j-1]+arr[i-1][j])
            arr[i].append(1)
        return arr

s = Solution()
arr = s.generate(15)
print(arr)