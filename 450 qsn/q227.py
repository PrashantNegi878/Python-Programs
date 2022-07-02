def minimumPlatform(self, n, arr, dep):
newarr = []
arr.sort()
dep.sort()
j = 0
tot = 1
for i in range(1, n):
    if arr[i] <= dep[j]:
        tot += 1
    else:
        j += 1

return tot
