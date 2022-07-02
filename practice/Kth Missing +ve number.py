arr=[1,2,3,4]
k=2
i=1
count=0
while True:
    if i not in arr:
        count+=1
    if count==k:
        print(i)
        break
    i+=1