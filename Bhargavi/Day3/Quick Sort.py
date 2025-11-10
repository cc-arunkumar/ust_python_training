# Quick Sort
def quick_sort(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)
        quick_sort(arr, low, pi - 1)
        quick_sort(arr, pi + 1, high)

def partition(arr, low, high):
    pivot = arr[high]
    j = low
    i = j - 1

    while j < high:
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
        j += 1

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1
arr = [20,30,50,89,100,12]
quick_sort(arr, 0, len(arr) - 1)
print("Sorted array:", arr)


# Sorted array: [12, 20, 30, 50, 89, 100]