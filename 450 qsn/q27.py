def isSubset( a1, a2, n, m):
    flag=0
    flag2=0
    for i in range(len(a2)):
        flag=0
        for j in range(len(a1)):
            if a2[i]==a1[j]:
                flag+=1
        if flag==0:
            flag2+=1
    if flag2>0:
        return("No")
    else:
        return("Yes")