a="UDLR"
x=0
y=0
for i in a:
    if i=="U":
        y+=1
    elif i=="D":
        y-=1
    elif i=="L":
        x-=1
    elif i=="R":
        x+=1
if x==0 and y==0:
    print(True)
else:
    print(False)
