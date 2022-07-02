t=int(input())
while t>0:
    x, y,n = input().split()
    x=int(x)
    y=int(y)
    xarr=[]
    yarr=[]
    xarr.append(0)
    yarr.append(0)
    for i in range(int(n)):
        x1,y1=input().split()
        x1=int(x1)
        y1=int(y1)
        xarr.append(x1)
        yarr.append(y1)
    xarr.append(x+1)
    yarr.append(y+1)
    xarr.sort()
    yarr.sort()
    for i in range(len(xarr)-1):
        xarr[i]=xarr[i+1]-xarr[i]-1
    for i in range(len(yarr)-1):
        yarr[i]=yarr[i+1]-yarr[i]-1
    # xarr.remove(len(xarr))
    xarr.pop()
    yarr.pop()
    total=max(xarr)*max(yarr)
    print(total)
    t-=1