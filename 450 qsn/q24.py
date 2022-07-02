def findLongestConseqSubseq(self, arr, N):
    arr.sort()
    count = 1
    maxcount = 1
    for i in range(1, N):
        if arr[i] == arr[i - 1] + 1:
            count += 1
            if count > maxcount:
                maxcount = count
        elif arr[i] == arr[i - 1]:
            pass
        else:
            count = 1
    return maxcount