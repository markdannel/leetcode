x = -1231231567

isNag = False
if x < 0:
    isNag = True
    x = abs(x)

l = len(str(x))

i = 0
temp = []
while i < l:
    temp.append(x%10)
    x = x//10
    i += 1

i = 0
num = 0
while i < l:
    num += temp[l-1-i]*10**i
    i += 1

if isNag:
    num *= -1

if num > 2**31-1 or num < -2**31:
    print("is 0")
print(num)
