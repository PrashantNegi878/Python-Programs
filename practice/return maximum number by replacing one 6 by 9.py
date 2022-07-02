num=9666
sum=str(num)
# arr=[]
# sum=""
# for i in str(num):
#     arr.append(i)
# for i in range(len(arr)):
#     if arr[i]=="6":
#         arr[i]="9"
#         break
# for i in arr:
#     sum=sum+i
# print(int(sum))
for i in range (len(sum)):
    if sum[i]=="6":
        break
sum=sum.replace("6","9",1)
print(sum)