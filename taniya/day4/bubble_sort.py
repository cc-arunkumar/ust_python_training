# Bubble Sort Implementation
lis1 = [16, 14, 5, 6, 8]   # Initial unsorted list

# Outer loop: runs (n-1) times where n = length of list
for i in range(len(lis1) - 1):
    check = False  # Flag to detect if any swap happened in this pass
    
    # Inner loop: compare adjacent elements
    for j in range(len(lis1) - i - 1):
        # If current element is greater than next, swap them
        if lis1[j] > lis1[j + 1]:
            lis1[j], lis1[j + 1] = lis1[j + 1], lis1[j]
            check = True  # Swap happened
    
    # If no swap happened in this pass, list is already sorted → break early
    if check == False:
        break

# Print the sorted list
print("Sorted list(bubble sort)", lis1)

# -------------------------
# Expected Output:
# Sorted list(bubble sort) [5, 6, 8, 14, 16]