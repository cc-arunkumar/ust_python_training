#Insertion sort

arr=[50,60,100,1,4]
n=len(arr)
# for i in range(n):
#     j=i
#     while j>0 and a[j-1]>a[j]:
#         a[j],a[j-1]=a[j-1],a[j]
#         j-=1
# print(a)

# List to be sorted
arr = [50, 60, 100, 1, 4]

# Insertion sort algorithm
for i in range(1, len(arr)):
    key = arr[i]  # Element to be inserted into the sorted part of the array
    j = i - 1  # Index of the last element in the sorted part

    # Shift elements to the right to make space for the key
    while j >= 0 and key < arr[j]:
        arr[j + 1] = arr[j]  # Move element to the right
        j -= 1  # Move to the previous element

    # Insert the key in its correct position
    arr[j + 1] = key

# Print the sorted array
print("Sorted array:", arr)


# Sample output
# Sorted array: [1, 4, 50, 60, 100]
