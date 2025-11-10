def bubble_sort(arr):
    for i in range(len(arr)-1):
        is_swapped=False
        for j in range(len(arr)-i-1):
            if arr[j]>arr[j+1]:
                is_swapped=True
                arr[j],arr[j+1]=arr[j+1],arr[j]
        if is_swapped==False:
            break
    print(arr)

l=[23,54,34,5,6,1]
bubble_sort(l)