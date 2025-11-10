def insertion(arr):

    n = len(arr)
    for i in range(n):
        temp = i
        while temp > 0 and arr[temp-1] > arr[temp]:
            if True:
                arr[temp-1],arr[temp] = arr[temp],arr[temp-1]
                temp = temp - 1

    return arr

arr = [5,3,6,2,9,1]
print(insertion(arr))

# -----------------------------------------------------------------

#Sample Output
#[1, 2, 3, 5, 6, 9]