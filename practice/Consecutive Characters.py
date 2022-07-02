s="abbcccddddeeeeedcba"
largest=0
for i in range(len(s)):
    l=1
    for j in range(i+1,len(s)):
        if s[j]==s[i]:

            # print(s[j])
            l+=1
            # print("equal")
        else:
            break
    if l>largest:
        largest=l
print(largest)