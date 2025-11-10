#bubble Sort
arr = [16, 14, 5, 6, 8]

for i in range(len(arr) - 1):
    is_swap = False
    for j in range(len(arr) - i - 1):
        if arr[j] > arr[j + 1]:
            arr[j], arr[j + 1] = arr[j + 1], arr[j]
            is_swap = True
    if is_swap==False:
        break
print(arr)

#output:
# PS C:\Users\303379\day4_training> & C:/Users/303379/AppData/Local/Microsoft/WindowsApps/python3.13.exe c:/Users/303379/day4_training/bubble_sort.py
# [5, 6, 8, 14, 16]
# PS C:\Users\303379\day4_training> 