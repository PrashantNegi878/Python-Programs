# def checkPal(s):
#     a = s[::-1]
#     if s==a:
#         return 1
#     else:
#         return 0
#
# def partitions(s,l):
#     arr=[]
#     print(s)
#     for i in range(l+1):
#         for j in range(i+1, l+1):
#             temp1=s[i:j]
#             temp2=temp1[::-1]
#             # print(temp1,temp2)
#             if temp1==temp2:
#                 arr.append(temp1)
#     return arr
# s="PERRFECT"
# l=len(s)
# t=checkPal(s)
# if t==1:
#     if l%2==0:
#         print(s[:l//2])
#     else:
#         print(s[:(l // 2)+1])
# elif t==0:
#     arr=partitions(s,l)
#     print(arr)
n=30
flag=False
for j in range (11,20):
    flag=False
    for i in range(2,(j//2)+1):
        # print(i)
        if j%i==0:
            flag=True
            break
    if flag==False:
        print(j)