#Bubble sort

# List of numbers to be sorted
a = [50, 60, 100, 1, 4]

# Get the length of the list
n = len(a)

# Boolean variable to check if any swapping happened
Boolean = False

# Outer loop to traverse through all elements
for i in range(n):
    # Inner loop to perform comparisons and swaps
    for j in range(n - i - 1):
        if a[j] > a[j + 1]:
            a[j], a[j + 1] = a[j + 1], a[j]  # Swap elements if they are in the wrong order
            Boolean = True  # Set Boolean to True to indicate that a swap occurred
    if Boolean == False:
        break  # Exit the loop if no swap occurred in the inner loop

# Print the sorted array
print("Sorted array:", a)


# Sample output
# Sorted array: [1, 4, 50, 60, 100]






