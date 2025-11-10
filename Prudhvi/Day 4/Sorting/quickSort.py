def quick_sort(arr):
    if len(arr) <= 1:
        return arr 
    
    pivot = arr[len(arr) // 2]
    left = [x for x in arr if x < pivot] 
    middle = [x for x in arr if x == pivot] 
    right = [x for x in arr if x > pivot] 
    
    return quick_sort(left) + middle + quick_sort(right)


numbers = [12, 4, 5, 6, 7, 3, 1, 15]
print("Original list:", numbers)
sorted_list = quick_sort(numbers)
print("Sorted list:", sorted_list)


#Sample Output
# Original list: [12, 4, 5, 6, 7, 3, 1, 15]
# Sorted list: [1, 3, 4, 5, 6, 7, 12, 15]