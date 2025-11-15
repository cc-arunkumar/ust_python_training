#insertion sort:

# Initial unsorted list
arr = [5, 3, 6, 2, 9, 1]

# Outer loop: iterate through elements starting from index 1
for i in range(1, len(arr)):
    # Inner loop: compare current element with previous elements
    for j in range(i, 0, -1):
        # If current element is smaller than the previous one, swap them
        if arr[j] < arr[j - 1]:
            arr[j], arr[j - 1] = arr[j - 1], arr[j]
        else:
            # If current element is in correct position, stop inner loop
            break

# Print the sorted list
print("Sorted:", arr)

#output:
# PS C:\Users\303379\day4_training> & C:/Users/303379/AppData/Local/Microsoft/WindowsApps/python3.13.exe c:/Users/303379/day4_training/insertion.py
# Sorted: [1, 2, 3, 5, 6, 9]
# PS C:\Users\303379\day4_training> 