str = "   +01"

str = str.strip()
l = len(str)
arr = []
isNag = False

ford = ord(str[0])
if ford != 43 and ford != 45 and (ford >57 or ford < 48):
    print('first is ', str[0])

if ford >47 and ford < 58:
    arr.append(int(str[0]))
elif ford == 45: #'-'
    isNag = True

i = 1
while i < l:
    ford = ord(str[i])
    if ford > 47 and ford < 58:
        arr.append(int(str[i]))
    else:
        break
    i += 1

i = 0
l = len(arr)
num = 0

if l > 0 and arr[0] == 0:
    pass
while i < l:
    num += arr[l-1-i]*10**i
    i += 1
if isNag:
    num *= -1
if num > 2**31-1 or num < -2**31:
    #return -2**31
    pass
print(arr, num)