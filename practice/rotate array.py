arr=[1,2,3,4,5,6,7,8,9]
n=int(input("Enter value of n = "))
arr3=arr[n:len(arr)]+arr[0:n]
arr2=arr[len(arr)-n:len(arr)]+arr[0:len(arr)-n]
print("Right Rotate = ",arr2)
print("Left Rotate = ",arr3)
