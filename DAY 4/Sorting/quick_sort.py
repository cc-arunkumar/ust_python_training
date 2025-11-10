list1 = [4, 7, 3, 5, 1]

def quick_sort(arr, low, high):
    if low < high:
        pivot_index = partition(arr, low, high)
        quick_sort(arr, low, pivot_index - 1)
        quick_sort(arr, pivot_index + 1, high)

def partition(arr, low, high):
    pivot=arr[high]
    i=low-1

    for j in range(low, high):
        if arr[j]<pivot:
            i=i+1
            arr[i],arr[j]=arr[j],arr[i]

    arr[i+1],arr[high] = arr[high],arr[i+1]
    return i + 1

quick_sort(list1,0,len(list1)- 1)
print(list1)


# sample output

"""
[1, 3, 4, 5, 7]
"""