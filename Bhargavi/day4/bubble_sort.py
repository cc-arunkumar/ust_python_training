
# Defined a bubble sort function that repeatedly swaps adjacent elements if they are in the wrong order.
# Used nested loops: outer loop for passes, inner loop for comparisons.
# Returned the sorted list after all passes.
# Tested the function with a sample list and printed the sorted result.

# Bubble Sort function
def bubble_sort(arr):
    n = len(arr)  # get length of the list
    # Outer loop for passes
    for i in range(n - 1): 
        # Inner loop for comparisons in each pass
        for j in range(n - i - 1):  
            # Swap if the current element is greater than the next
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]  
    return arr  # return the sorted list


my_list = [89, 45, 21, 10, 35, 100]

# Call bubble sort
sorted_list = bubble_sort(my_list)

# Print the sorted array
print("sorted array =", sorted_list)

#  Output:
# sorted array = [10, 21, 35, 45, 89, 100]
