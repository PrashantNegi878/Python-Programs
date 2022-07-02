a=[1,10,3,4,5,6,7]
l = len(a)
j = 0
a.sort()
k=int(input())
print(a)
print(f"{k} th Min. Number = {a[k-1]}")
print(f"{k} th Max. Number = {a[len(a)-k]}")




