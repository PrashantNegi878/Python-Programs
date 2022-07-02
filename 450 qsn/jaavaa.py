# a="AAABBBCDEAABBCZZZ"
# print(a)
# b=list(set(a))
# c=[]
# tot=0
# for i in b:
#     tot=0
#     for j in a:
#         if i==j:
#             tot+=1
#     c.append(tot)
# print(b)
# print(c)
#
# for i in range(0,len(c)):
#     for j in range(0,len(c)):
#         if c[j]>c[i] and i!=j:
#             temp=c[i]
#             c[i]=c[j]
#             c[j]=temp
#             temp2=b[i]
#             b[i]=b[j]
#             b[j]=temp2
# print(c)
# print(b)


a="AACDDEB"
b="AEBBFR"

a1=list(set(a))
b1=list(set(b))
c1=[]
d1=[]
for i in a1:
    for j in b1:
        if i==j:
            c1.append(i)
for i in a1:
    if i not in c1:
        d1.append(i)
for i in b1:
    if i not in c1:
        d1.append(i)
c1.sort()
d1.sort()
print(c1)
print(d1)