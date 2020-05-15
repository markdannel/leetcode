# 给定一个整数数组  nums，求出数组从索引 i 到 j  (i ≤ j) 范围内元素的总和，包含 i,  j 两点。

# 示例：

# 给定 nums = [-2, 0, 3, -5, 2, -1]，求和函数为 sumRange()

# sumRange(0, 2) -> 1
# sumRange(2, 5) -> -1
# sumRange(0, 5) -> -3
# 说明:

# 你可以假设数组不可变。
# 会多次调用 sumRange 方法。

class NumArray:

    def __init__(self, nums: [int]):
        l=len(nums)
        if l==0:return
        self.arrs=[0 for i in range(l+1)]
        self.arrs[l-1]=nums[l-1]
        for i in range(len(nums)-2,-1,-1):
            self.arrs[i] = self.arrs[i+1] + nums[i]

    def sumRange(self, i: int, j: int) -> int:
        return self.arrs[i]-self.arrs[j+1]
s = NumArray([])
print(s.sumRange(0,2))
print(s.sumRange(2,5))
print(s.sumRange(0,5))


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)