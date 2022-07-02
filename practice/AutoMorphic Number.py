def findAutoMorphic(n):
    nsqur=int(n)*int(n)
    if n in str(nsqur):
        return 1
    else:
        return 0

a=input("Enter 1st no = ")
a1=findAutoMorphic(a)
if a1==1:
    print("Automorphic Number")
else:
    print("Not an Automorphic Number")