def quicksort(arr):
    if len(arr) <= 1:
        return arr
    else:
        key = arr[len(arr) // 2]
        left = [x for x in arr if x < key]
        mid = [x for x in arr if x == key]
        right = [x for x in arr if x > key]
        return quicksort(left) + mid + quicksort(right)
list1 = [4,8,1,3,9,7,5]
sort_list = quicksort(list1)
print(f"sorted list: {sort_list}")