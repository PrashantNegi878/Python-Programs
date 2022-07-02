a="baloon"
# text="loonbalxballpoon"
text="nlaebolko"
arr1=[]
arr2=[]
for i in range(len(a)):
    if not arr1.count(a[i])>0:
        arr1.append(a[i])

for i in range(len(arr1)):
    arr2.append(text.count(arr1[i]))
arr2[3]=arr2[3]/2
# print(arr1)
# print(arr2)
print(min(arr2))
