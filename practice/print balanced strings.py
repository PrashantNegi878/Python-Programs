s="RLLLLRRRLR"
balance=0
total=0
for i in s:
    if i=="R":
        balance-=1
    if i=="L":
        balance+=1
    if balance==0:
        total+=1
print(total)


