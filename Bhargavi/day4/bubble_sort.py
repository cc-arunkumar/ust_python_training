#bubble sort
def bubble_sort(arr):
    n = len(arr)
    for i in range(n - 1): 
        for j in range(n - i - 1):  
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]  
    return arr  
my_list = [89, 45, 21, 10, 35, 100]
sorted_list = bubble_sort(my_list)
print("sorted array =", sorted_list)


#sorted array = [10, 21, 35, 45, 89, 100]
