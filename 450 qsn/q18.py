class Solution:
    def getPairsCount(self, arr, n, k):
        count = 0
        arr.sort()
        for i in range(0, n):
            for j in range(i + 1, n):
                if arr[i] + arr[j] > k:
                    break
                if arr[i] + arr[j] == k:
                    count += 1
                    # print(arr[i],arr[j])
                    # print(i,j)

        return count

    #or 2nd method

    # class Solution:
    #     def getPairsCount(self, arr, n, k):
    #         count = 0
    #         arr.sort()
    #         for i in range(n - 1, -1, -1):
    #             if arr[i] != k - arr[i] and k - arr[i] in arr:
    #                 count += arr.count((k - arr[i]))
    #                 arr.pop(i)
    #             elif arr[i] == k - arr[i]:
    #                 count += arr.count((arr[i])) - 1
    #                 arr.pop(i)
    #         return count