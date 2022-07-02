def factorial(self, N):
    sum = 1
    j = 0
    for j in range(1, N + 1):
        sum = sum * j
    s = [sum]
    return s