s="How many eggs in 12### a,  dozen 13?"
arr=list(s.split())
print(arr)
count=0
temp="False"
# for i in range (len(arr)):
#     temp = "False"
#     for j in range (len(arr[i])):
#         if arr[i][j].isdigit():
#             temp="True"
#     if temp=="False":
#         count+=1
# print(count)
for i in range (len(arr)):
    temp = "False"
    for j in range (len(arr[i])):
        if arr[i][j].isalpha():
            temp="True"
    if temp=="True":
        count+=1
print(count)
