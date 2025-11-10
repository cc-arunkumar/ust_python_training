# Task: Insertion Sort
# Scenario:
# Sort a list of numbers in ascending order using the insertion sort algorithm.

arr = [10, 4, 7, 18, 1, 2]

# Insertion sort logic
for i in range(1, len(arr)):
    for j in range(i, 0, -1):
        if arr[j] < arr[j - 1]:
            arr[j], arr[j - 1] = arr[j - 1], arr[j]
        else:
            break  # Exit inner loop early if already in order

print("Sorted:", arr)

# Sample Output:
# Sorted: [1, 2, 4, 7, 10, 18]
