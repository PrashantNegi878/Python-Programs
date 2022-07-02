# a=[1,10,3,4,5,6,7]
a = (input())
l = len(a)
b = []
j = 0
for i in range(l):
    b.append(int(a[(l - 1) - i]))
print(b)
