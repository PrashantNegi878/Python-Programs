a="hello world"
arr=[]
for i in a:
    if arr.count(i)<=0:
        arr.append(i)
for i in arr:
    print(f'{i} = {a.count(i)}',end=", ")

