a=[1, 4, 45, 6, 0, 19]
x=51
maxx=max(a)
i=a.index(maxx)
count=1
left=i-1
right=i+1
print(f"left = {left}, rigth = {right}")
while maxx<x:
    print(f"left = {left}, rigth = {right}")
    if left==-1:
        maxx = maxx + a[right]
        print("add rigth", a[right])
        right += 1
        count+=1
        continue
    if right==len(a):
        maxx = maxx + a[left]
        print("add left", a[left])
        left -= 1
        count += 1
        continue
    if a[left]>=a[right]:
        maxx=maxx+a[left]
        print("add left",a[left])
        left-=1
    elif a[right]>=a[left]:
        maxx=maxx+a[right]
        print("add rigth", a[right])
        right+=1
    count+=1
print(count)