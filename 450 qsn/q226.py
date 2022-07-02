n=3
total=0
arr=[[1,1000,1030,1],
     [2,1010,1030,1],
     [3,1000,1020,2],
     [4,1030,1230,2],
     [5,1200,1230,3],
     [6,900,1005,1]]
# arr=[[1,1000,1030,1],
#      [2,1110,1130,1],
#      [3,1200,1220,1]]
arr.sort(key=lambda x:x[2])
# print(arr)
checkarr=[-1 for i in range (n+1)]
print(arr)
for i in range (len(arr)):
    if checkarr[arr[i][3]]==-1:
        checkarr[arr[i][3]]=arr[i]
        total+=1
    elif checkarr[arr[i][3]][2]<arr[i][2]:
        checkarr[arr[i][3]] = arr[i]
        total+=1

# print(checkarr)
print(total)