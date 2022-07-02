t=int(input())
a1=[]
for i in range(t):
    h,a=input().split()
    a1.append([h,a])
for i in range(t):
    h=int(a1[i][0])
    a = int(a1[i][1])
    # print(h,a)
    time=0
    while h>0 and a>0:
        # print(h,a)
        if time%2==0:
            h+=3
            a+=2
            time+=1
        elif h>20:
            h-=20
            a+=5
            time+=1
        else:
            h-=5
            a-=10
            time+=1
        # print(h,a)
        # print(time)
    print(time-1)
    # t-=1