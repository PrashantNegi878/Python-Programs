def candyStore(self, candies, N, K):
    candies.sort()
    low = 0
    high = 0
    temp = 0
    count = 0
    while temp < N:
        count += 1
        temp += K + 1
    for i in range(count):
        low = low + candies[i]
        high = high + candies[N - 1 - i]
    # print(low,high)

    return (low, high)