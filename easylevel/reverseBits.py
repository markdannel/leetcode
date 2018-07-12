class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        def hammingWeight(n):
            count = 0
            arr = [0]*32
            while n:
                if n%2 == 1:
                    arr[count] = 1
                n = n//2
                count += 1
            return arr
        arr = hammingWeight(n)
        print(arr)
        arr.reverse()
        print(arr)
        sum = 0
        for i in range(0, len(arr)):
            sum += arr[i]*2**i
            if arr[i]: print(2**i)
        return sum
s = Solution()
n = s.reverseBits(0)
print(n)