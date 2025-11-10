#Bubble Sort


def bubble_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        for j in range(n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr

my_list = [53, 87, 12, 22, 16]
sorted_list = bubble_sort(my_list)
print("Sorted array =", sorted_list)

#o/p:
# Sorted array = [12, 16, 22, 53, 87]