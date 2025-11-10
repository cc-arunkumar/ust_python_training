def quick(arr):

    if len(arr) <= 1:
        return arr

    pivot = arr[0]
    left = []
    right = []

    for  i in range(1,len(arr)):
        if arr[i] < pivot:
            left.append(arr[i])
        else:
            right.append(arr[i])

    return quick(left) + [pivot] + quick(right)

arr = [20,16,5,6,4]
print(quick(arr))

# --------------------------------------------------------------------

# Sample Output
# [4, 5, 6, 16, 20]

