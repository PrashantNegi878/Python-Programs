x=0
y=0
path="NES"
arr=[]
arr.append("00")
chk=False
for i in path:
    if i=="N":
        y+=1
    elif i=="S":
        y-=1
    elif i=="E":
        x+=1
    elif i=="W":
        x-=1
    if (str(x)+str(y) in arr):
        arr.append(str(x) + str(y))
        chk=True
    else:
        arr.append(str(x)+str(y))
print(arr)
print(chk)
