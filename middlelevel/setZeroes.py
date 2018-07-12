class Solution:
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        l = len(matrix)
        if l == 0:
            return matrix
        r = len(matrix[0])
        larr = [1]*l
        rarr = [1]*r
        for i in range(0, l):
            for j in range(0, r):
                if matrix[i][j] == 0:
                    larr[i] = 0
                    rarr[j] = 0
        for i in range(0, l):
            if larr[i] == 0:
                matrix[i] = [0]*r
        for i in range(0, r):
            if rarr[i] == 0:
                for j in range(0, l):
                    matrix[j][i] = 0
        return matrix
arr = [[1,1,1],[1,0,1],[1,1,1]]
# arr = [
#   [0,1,2,1],
#   [3,4,5,2],
#   [1,3,0,5]
# ]
s = Solution()
res = s.setZeroes(arr)
print(res)