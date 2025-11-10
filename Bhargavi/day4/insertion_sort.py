#Insertion Sort
def insertion_sort(arr):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key

num = [33,45,78,90,11,22,33]
insertion_sort(num)
print("Sorted array:", num)

# Sorted array: [11, 22, 33, 33, 45, 78, 90]