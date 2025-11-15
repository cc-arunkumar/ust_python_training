#bubble Sort
# Initial unsorted list
arr = [16, 14, 5, 6, 8]

# Outer loop: runs for each pass (n-1 passes in worst case)
for i in range(len(arr) - 1):
    is_swap = False  # Flag to check if any swap happened in this pass
    
    # Inner loop: compares adjacent elements
    for j in range(len(arr) - i - 1):
        # If the current element is greater than the next, swap them
        if arr[j] > arr[j + 1]:
            arr[j], arr[j + 1] = arr[j + 1], arr[j]  # Swap values
            is_swap = True  # Mark that a swap occurred
    
    # If no swaps happened in this pass, list is already sorted → break early
    if is_swap == False:
        break

# Print the sorted list
print(arr)


#output:
# PS C:\Users\303379\day4_training> & C:/Users/303379/AppData/Local/Microsoft/WindowsApps/python3.13.exe c:/Users/303379/day4_training/bubble_sort.py
# [5, 6, 8, 14, 16]
# PS C:\Users\303379\day4_training> 