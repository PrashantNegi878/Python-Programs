dict={
    "I":1,
    "V":5,
    "X":10,
    "L":50,
    "C":100,
    "D":500,
    "M":1000
}
sum=0
s="XXIVIX"
temp=0
for i in range(len(s)):
    sum=sum+dict[s[i]]
    if dict[s[i]]>temp:
        sum=sum-2*temp
    temp=dict[s[i]]
print(sum)



