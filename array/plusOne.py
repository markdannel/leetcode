digits = [9,9,9,9]

l = len(digits)

i = 0
sum = 0
while i < l:
    sum += digits[l-1-i]*10**i
    i += 1

sum += 1

i = 0
res = []
l = len(str(sum))
while i < l:
    lastn = sum%10
    sum //= 10
    res.insert(0, lastn)
    i += 1
print(res)

