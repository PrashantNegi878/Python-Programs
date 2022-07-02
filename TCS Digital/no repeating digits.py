a,b=map(int,input().split())
count=0
for i in range(a,b):
    if len(str(i))==len(set(str(i))):
        count+=1
print(count)