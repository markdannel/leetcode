def maxProfit(prices):
    maxp = 0
    minp = prices[0]
    for i in prices:
        minp = min(minp, i)
        maxp = max(maxp, i- minp)
    return maxp

prices = list(range(999, 0, -1))#[7,1,5,3,6,4]
prices.append(5)
print(maxProfit(prices))