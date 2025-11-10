def Partition(list1, l, h):
    pivot = list1[l]
    i = l
    j = h
    while i < j:
        while pivot >= list1[i] and i <= h:
            i = i + 1
        while pivot < list1[j] and j >= l:
            j = j - 1
        if i < j:
            list1[i], list1[j] = list1[j], list1[i]
    list1[j], list1[l] = list1[l], list1[j]
    return j

def Quicksort(list1, l, h):
    if l < h: 
        ind = Partition(list1, l, h)
        Quicksort(list1, l, ind - 1)
        Quicksort(list1, ind + 1, h)

list1 = [2, 4, 3, 1, 0, 9]
print(list1)
Quicksort(list1, 0, len(list1) - 1)
print(list1)
