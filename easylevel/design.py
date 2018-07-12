import random
class Solution:
	def __init__(self, nums):
		self.nums = nums
	
	def reset(self):
		return self.nums

	def shuffle(self):
		'''
		temp = []
		nn = self.nums.copy()
		for num in nums:
			temp.append(num)
		return temp
		'''
		temp = self.nums.copy()
		random.shuffle(temp)
		return temp

nums = [1,2,3,4,5]
sol = Solution(nums)
print(sol.shuffle())
print(sol.reset())
print(sol.shuffle())
print(sol.reset())
