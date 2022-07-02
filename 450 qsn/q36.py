# ar1 = [2, 3, 5, 8]
# ar2= [10, 12, 14, 16, 18, 20]
#
# for i in ar2:
#     ar1.append(i)
# ar1.sort()
# l=len(ar1)
# if l % 2 != 0:
#     median = ar1[l//2]
# else:
#     median = (ar1[l//2] + ar1[l//2 - 1]) // 2
# print(median)

i = int(input("Enter no.1 = "))
j = int(input("Enter no.2 = "))
j2=0
inc=1
if (i%j==0):
    print(f"{j} is Divisible by {i}")
else:
    while(j2<j):
        j2=i*inc
        inc+=1
    print(f"The closest no. to {j} divisible by {i} is {j2}")

