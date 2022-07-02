def maxProfit(self, prices):
    a1 = []
    mx = 0
    finalmx = 0
    for i in range(len(prices) - 1, -1, -1):
        if prices[i] > mx:
            mx = prices[i]
        a1.append(mx)
    a1.reverse()
    for i in range(len(prices)):
        if a1[i] - prices[i] > finalmx:
            finalmx = a1[i] - prices[i]
    return finalmx