def partition(Array, l, r):
    i = l
    j = r
    pivot = Array[l]
    while (i < j):
        while (Array[i] <= pivot and i < j):
            i = i + 1
        while (Array[j] > pivot):
            j = j - 1
        if (i < j):
            Array[i], Array[j] = Array[j], Array[i]
    Array[l],Array[j]=Array[j],Array[l]
    return j


def quick(Array, l, r):
    if (l >= r):
        return
    piv = partition(Array, l, r)
    quick(Array, l, piv - 1)
    quick(Array, piv + 1, r)


# Array = [90,48, 44, 19, 59, 72, 80, 42, 65, 82, 8, 95, 68]
Array=[10,11,9,8,7,6,5,4,3,2,1]
low = 0
up = len(Array) - 1
quick(Array, low, up)
print(Array)