s="loveleetcode"
c="e"
arr=[]
j=1
for i in range(len(s)):
    if s[i]==c:
        arr.append(0)
    else:
        j=1
        while j<len(s):
            if (i+j)<len(s) and s[i+j]==c:
                arr.append(j)
                break
            elif (i-j)>0 and s[i-j]==c:
                arr.append(j)
                break
            j+=1
print(arr)