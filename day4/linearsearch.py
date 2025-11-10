# Linear Search 

def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i   
    return -1   


numbers = [4, 2, 7, 1, 9, 3]
print("List:", numbers)

x = int(input("Enter number to search: "))
result = linear_search(numbers, x)

if result != -1:
    print("Element found at index", result)
else:
    print("Element not found")

# List: [4, 2, 7, 1, 9, 3]
# Enter number to search: 6
# Element not found

# List: [4, 2, 7, 1, 9, 3]
# Enter number to search: 2
# Element found at index 1