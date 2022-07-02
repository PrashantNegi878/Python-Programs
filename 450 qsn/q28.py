
def find3Numbers(self, A, n, X):
    A.sort()
    count = 0
    for i in range(n):
        l = 0
        r = n - 1
        while l != r:
            if A[i] + A[l] + A[r] == X and i != l and i != r:
                count += 1
                break
            elif A[i] + A[l] + A[r] >= X:
                r -= 1
            elif A[i] + A[l] + A[r] <= X:
                l += 1
    return count
