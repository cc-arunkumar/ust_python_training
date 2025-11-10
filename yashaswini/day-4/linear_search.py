# Linear Search
 
def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i  
    return -1  
 
numbers = [3,9,15,21,30]
print("List:", numbers)
 
x = int(input("Enter number to search: "))
result = linear_search(numbers, x)
if result != -1:
    print("Element found at index", result)
else:
    print("Element not found")

#o/p:
# List: [3, 9, 15, 21, 30]
# Enter number to search: 15
# Element found at index 2

# List: [3, 9, 15, 21, 30]
# Enter number to search: 6
# Element not found