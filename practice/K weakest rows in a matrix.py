mat=[[1,1,0,0,0],
     [1,1,1,1,0],
     [1,0,0,0,0],
     [1,1,0,0,0],
     [1,1,1,1,0]]
arr2=[]
for i in range(len(mat)):
    arr2.append([i,mat[i].count(1)])
arr2.sort(key=lambda x:x[1])
print(arr2)