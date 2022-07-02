stack1=[1,1,1,2,3]
stack2=[2,3,4]
stack3=[1,4,5,2]
s1=sum(stack1)
s2=sum(stack2)
s3=sum(stack3)
s4=[]
while s1!=s2 or s1!=s3 or s2!=s3:
    # print(s1,s2,s3)
    if s1 >= s2 and s1 >= s3:
         stack1.pop()
    elif s2 >= s1 and s2 >= s3:
         stack2.pop()
    elif s3 >= s1 and s3 >= s2:
         stack3.pop()
    s1 = sum(stack1)
    s2 = sum(stack2)
    s3 = sum(stack3)
    print(s1,s2,s3)
print(s1)
