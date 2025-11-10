#  Insertion Sort 
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i] 
        j = i - 1  
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]  
            j -= 1
        arr[j + 1] = key
    return arr
numbers = [30, 34, 61,48, 13, 16, 90]
numbers = insertion_sort(numbers)
print("Sorted array is:", numbers)

# Sorted array is: [13, 16, 30, 34, 48, 61, 90]