def climbStairs(n):
    arr = [1,2,3]
    if n == 0: return 0
    def fn(n):
        l = len(arr)
        if l >= n:
            return int(arr[n-1])
        elif l+1 == n:
            arr.append(arr[l-1]+arr[l-2])
            return arr[l]
        else:
            num = fn(n-2)+fn(n-1)
            return num
    return fn(n)
print(climbStairs(350))
