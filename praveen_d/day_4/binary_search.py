arr = [2, 3, 4, 10, 40]
x = 10

low, high = 0, len(arr) - 1

while low <= high:
    mid = low + (high - low) 
    if arr[mid] == x:
        print(f"Found at index: {mid}")
        break
    elif arr[mid] < x:
        low = mid + 1
    else:
        high = mid - 1
else:
    print("Not found")

# EXPECTED OUTPUT
# Found at index: 3