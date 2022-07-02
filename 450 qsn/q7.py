# a[] = [0, 1, 2, 3, 4, 5, 6]
n=int(input("Enter no. of elements = "))
a=[]
for i in range (0,n):
    element=int(input())
    a.append(element)

l = len(a)
temp = a[l - 1]
for i in range(l - 1, 0,-1):
    a[i] = a[i - 1]
a[0] = temp
print(a)
