l=int(input("Length of array = "))
arr=[]
for i in range(l):
    arr.append(int(input("Enter element  = ")))
n=int(input("Enter rotation count = "))
arr=arr[len(arr)-n:len(arr)]+arr[:len(arr)-n]
print(arr)
