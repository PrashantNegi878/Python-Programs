# not complete
min = arr[0]
max = arr[0]
sum = 0
for i in arr:
    if i < min:
        min = i
    if i > max:
        max = i
avg = min + max / 2
for i in range(0, n):
    if arr[i] > avg:
        arr[i] = arr[i] - k
    else:
        arr[i] = arr[i] + k
for i in arr:
    if i < min:
        min = i
    if i > max:
        max = i

return ((max - k) - (min + k))