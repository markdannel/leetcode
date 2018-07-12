class Solution:
	def fizzBuzz(self, n):
		arr = []
		flag = False
		i = 1
		while i <= n:
			if i%3 == 0:
				arr.append('Fizz')
				flag = True
			if i%5 == 0:
				if flag:
					arr[i-1] = 'FizzBuzz'
				else:
					arr.append('Buzz')
				flag = True
			if not flag:
				arr.append(str(i))
			flag = False
			i += 1
		return arr
s = Solution()
print(s.fizzBuzz(50))
