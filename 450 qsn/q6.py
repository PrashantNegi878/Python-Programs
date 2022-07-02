a = [0, 1, 2, 3, 4, 5, 6]
b = [0, 2, 4, 6,8,10]
c=a
d=[]
for i in b:
        flag=0
        for j in a:
           if i==j:
               flag+=1
        if flag==0:
            c.append(i)
print(f"Union = {c}")

for i in a:
        for j in b:
           if i==j:
               d.append(i)
print(f"Intersection = {d}")



