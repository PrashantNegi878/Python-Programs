class Solution:
    def count(self, S, m, n):
        # code here
        arr = [[0 for i in range(n + 1)] for j in range(len(S))]
        for i in range(len(S)):
            arr[i][0] = 1
        for i in range(1):
            for j in range(n + 1):
                if j % S[i] == 0:
                    arr[i][j] = 1
        # print(arr)

        for i in range(1, len(S)):
            for j in range(n + 1):
                # print(S[i],j)
                if S[i] > j:
                    arr[i][j] = arr[i - 1][j]
                # elif S[i]%j==0:
                # arr[i][j]=1
                else:
                    arr[i][j] = arr[i - 1][j] + arr[i][j - S[i]]
        return (arr[len(S) - 1][n])