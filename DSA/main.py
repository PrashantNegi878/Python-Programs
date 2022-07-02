def turnPigeons(A):
    arr=[]
    for i in A:
        if len(arr)==0:
            arr.append(i)
        elif arr[-1]=='L' and i=='R':
            # arr.pop()
            pass
        elif arr[-1]=='R' and i=='L':
            pass
            # arr.pop()
        else:
            arr.append(i)
    print(len(arr))

A='LLLRRRR'
turnPigeons(A)
