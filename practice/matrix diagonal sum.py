mat=[[1,2,3],
     [4,5,6],
     [7,8,9]]
lenmat=len(mat)
sum=0
lenin=len(mat[1])
for i in range(lenmat):
    sum=sum+mat[i][i]
    # print(mat[i][i])
for i in range(lenmat):
    sum=sum+mat[i][lenin-1-i]
    # print(mat[i][lenin-1-i])
if lenmat%2!=0:
    sum=sum-mat[lenmat//2][lenmat//2]
print(sum)