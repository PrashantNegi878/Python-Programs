mat= [[1,10,4,2],
     [9,3,8,7],
     [15,16,17,12]]
lucky=mat[0][0]
for i in range(len(mat)):
    temp=min(mat[i])
    if temp>lucky:
        lucky=temp
print(lucky)