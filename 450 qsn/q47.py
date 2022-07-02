mat = [[1, 2, 1, 4, 8],
       [3, 7, 8, 5, 1],
       [8, 7, 7, 3, 1],
       [8, 1, 2, 7, 9]]
rows = len(mat)
columns = len(mat[0])
count = 0
tcount = 0
arr = []
mat1 = list(set(mat[0]))
for i in mat1:
    tcount = 0
    for j in range(1, rows):
        count = 0
        for k in range(columns):
            if i == mat[j][k]:
                count = 1
        tcount = tcount + count
    if tcount == 3:
        arr.append(i)

print(arr)