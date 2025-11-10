# Task: Bubble Sort
# Scenario:
# Implement bubble sort to arrange elements of a list in ascending order.

def bubble_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr  # ✅ Corrected indentation — outside both loops

# Given list
my_list = [89, 45, 21, 10, 35, 100]
sorted_list = bubble_sort(my_list)
print("Sorted array =", sorted_list)

# Sample Output:
# Sorted array = [10, 21, 35, 45, 89, 100]
