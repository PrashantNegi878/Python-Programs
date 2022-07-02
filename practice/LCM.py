# a=int(input("Enter no.1 = "))
# b=int(input("Enter no.2 = "))
# i=max(a,b)
# arr=0
# while 1:
#     if i%a==0 and i%b==0:
#         arr=i
#         break
#     i+=1
# print(arr)
# class N():
#     def over(self,n=None,x=None,y=None):
#         if x==None and y==None and n==None:
#             print("this is none")
#         elif x==None and y==None:
#             print(f"this is n {n}")
#         elif y == None:
#                 print(f"this is x,n {x,n}")
#         else:
#             print(f"this is x,y,n {x,y,n}")
#
# o=N()
# o.over()
# o.over(1)
# o.over(1,2)
# o.over(1,2,3)
# class A():
#     def overr(self):
#         print("Fn1")
#
# class B(A):
#     def overr(self):
#         print("Fn2")
#
# obj1=B()
# obj1.overr()
for i in range(2,50):
    check=False
    for j in range(2,(i//2)+1):
        if i%j==0:
            check=True
    if check==False:
        print(i)







