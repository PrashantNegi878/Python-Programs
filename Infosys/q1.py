n=int(input())
exp=int(input())
temp=0
bosspow=[]
bonus=[]
count=0
for i in range(n):
    temp=input()
    bosspow.append(int(temp))
for i in range(n):
    temp=input()
    bonus.append(int(temp))
# print(bosspow)
# print(bonus)
keep=[]
i=n-1
while i>=0:
    print(f'experience = {exp}')
    print(f'Boss Power  = {bosspow[i]}')
    # print(f'n = {n}' )
    if bosspow[i]<=exp:
        count+=1
        print(f'(defeated) experience = {exp}')
        print(f'(defeated)Boss Power  = {bosspow[i]}')
        exp = exp + bonus[i]
        keep.append(bosspow.pop(i))
        bonus.pop(i)
        n=n-1
        i=n
    i-=1
# print(bosspow)
# print(bonus)
print(f'count = {count}')
print(keep)
print(exp)

