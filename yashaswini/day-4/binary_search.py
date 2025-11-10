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
 
numbers = [4,16,24,32,40]
print("List:", numbers)
 
x = int(input("Enter number to search: "))
result = binary_search(numbers, x)
 
if result != -1:
    print("Element found at index", result)
else:
    print("Element not found")


#o/p:
# List: [4, 16, 24, 32, 40]
# Enter number to search: 32
# Element found at index 3

# List: [4, 16, 24, 32, 40]
# Enter number to search: 8
# Element not found