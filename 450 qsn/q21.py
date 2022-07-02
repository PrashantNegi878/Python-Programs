def subArrayExists(self, arr, n):
    s = 0
    a2 = []
    for i in arr:
        s += i
        a2.append(s)
    hm = {}
    for i in a2:
        if i == 0 or i in hm:
            return True
            break
        hm[i] = 1
    return False
