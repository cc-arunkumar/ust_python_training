#linear search
def linear_search(arr, target):
    for index in range(len(arr)):
        if arr[index] == target:
            return index
    return -1


arr = [5, 3, 7, 9, 2]
target = 7

result = linear_search(arr, target)

if result != -1:
    print(f"Target {target} found at index {result}")
else:
    print(f"Target {target} not found in the list")



# Sample Output:
# Target 7 found at index 2

