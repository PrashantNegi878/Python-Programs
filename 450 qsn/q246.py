# arr=[5,-4,1,-3,1]

while 1:
    # n=10
    # print(n)
    n = int(input())
    t=0
    if n==0:
        break
    #arr =[int(x) for x in input().split()]
    arr = list(map(int, input().split()))
    buyers=[]
    sellers=[]
    for i in range (len(arr)):
        if arr[i]>0:
            buyers.append([arr[i],i])
        elif arr[i]<0:
            sellers.append([arr[i], i])
    i=0
    j=0
    work=0
    while(i<len(buyers) and j<len(sellers)):
        temp=min(buyers[i][0],-sellers[j][0])
        buyers[i][0]=buyers[i][0]-temp
        sellers[j][0]=sellers[j][0]+temp
        tempwrk=temp*abs(buyers[i][1]-sellers[j][1])
        work+=tempwrk
        if buyers[i][0]==0:
            i+=1
        if sellers[j][0]==0:
            j+=1
    print(work)
# a=list(map(int,input().split()))
# print(a)