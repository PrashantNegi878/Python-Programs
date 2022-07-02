def commonElements(self, A, B, C, n1, n2, n3):
    a = {}
    b = {}
    c = {}
    arr = []
    for i in A:
        a[i] = 1
    for i in B:
        b[i] = 1
    for i in C:
        c[i] = 1
    # A=list(set(A))
    for i in A:
        if i in a and i in b and i in c and i not in arr:
            arr.append(i)
    return arr