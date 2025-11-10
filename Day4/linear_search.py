def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i  
    return -1  

numbers = [4, 2, 7, 1, 9, 3]
target = 7
result = linear_search(numbers, target)
print("Linear Search Result at index:", result)


# Linear Search Result at index: 2