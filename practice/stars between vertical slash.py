s="*|*|****|"
s=" "+s+" "
# print(s)
print(f"({s})")
arr1=[1,2]
arr2=[7,8]
arr3=[]
leftslash=0
rightslash=0
count=0
for i in range(len(arr1)):
    count=0
    mid=arr1[i]+arr2[i]//2
    left = mid
    right = mid
    while(left>=arr1[i] or right<=arr2[i]):
        if s[left]=="|":
            leftslash = left
        if s[right] == "|":
            rightslash=right
        if left>=arr1[i]:
            left-=1
        if right<=arr2[i]:
            right+=1
    print(f"left = {left}, right = {right}")
    for j in range(leftslash,rightslash):
        if s[j]=="*":
            count+=1
            # print(i,j)
    arr3.append(count)
print(arr3)