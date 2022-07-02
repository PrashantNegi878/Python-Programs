def findMinDiff(self, A, N, M):
    i = 0
    temp = 0
    A.sort()
    minn = A[N - 1] - A[0]
    while (M - 1 + i < N):
        temp = A[M - 1 + i] - A[i]
        if temp < minn:
            minn = temp
        i += 1
    return minn