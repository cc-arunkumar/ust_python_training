# Binary Search 

def binary_search(arr, target):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2  
        if arr[mid] == target:
            return mid  
        elif arr[mid] < target:
            low = mid + 1   
        else:
            high = mid - 1  
    return -1   


numbers = [1, 3, 5, 7, 9, 11, 13]
print("List:", numbers)

x = int(input("Enter number to search: "))
result = binary_search(numbers, x)

if result != -1:
    print("Element found at index", result)
else:
    print("Element not found")

# List: [1, 3, 5, 7, 9, 11, 13]
# Enter number to search: 56
# Element not found

# List: [1, 3, 5, 7, 9, 11, 13]
# Enter number to search: 11
# Element found at index 5