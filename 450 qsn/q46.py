def kthSmallest(mat, n, k):
    a1=[]
    for i in range (n):
        for j in range (n):
            a1.append(mat[i][j])
    a1.sort()
    return(a1[k-1])