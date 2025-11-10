#Linear Search
def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

num= [22,45,89,23,44,77,99]
x = 25
result = linear_search(num, x)

if result != -1:
    print(f"Element found at index {result}")
else:
    print("Element not found")

# Element not found