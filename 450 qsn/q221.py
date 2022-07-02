class Solution:

    # Function to find the maximum profit and the number of jobs done.

    def JobScheduling(self, Jobs, n):

        # def func(p1, p2):
        #     return p1.profit > p2.profit

        # Jobs.sort(key = func)

        arr = []
        check = []
        total = 0
        max = 0
        for i in range(len(Jobs)):
            arr.append([Jobs[i].profit, Jobs[i].deadline])
            if Jobs[i].deadline > max:
                max = Jobs[i].deadline
        # print(arr)
        arr.sort()
        count = 0
        arr2 = []
        arr = list(reversed(arr))
        # print(arr)
        for i in range(max):
            check.append(False)

        for i in range(len(arr)):
            if check[arr[i][1] - 1] == False:
                check[arr[i][1] - 1] = True
                total += arr[i][0]
                count += 1
            else:
                for j in range(arr[i][1], 0, -1):
                    # check[arr[i][1]-1]>=0 and check[arr[i][1]-1]<len(check)
                    if check[j - 1] == False:
                        check[j - 1] = True
                        total += arr[i][0]
                        count += 1
                        break
        arr2.append(count)
        arr2.append(total)
        return (arr2)