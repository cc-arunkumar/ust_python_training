#binary search 

def binary_search(arr, target):
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2  

        if arr[mid] == target:
            return mid  
        elif arr[mid] < target:
            low = mid + 1 
        else:
            high = mid - 1 

    return "Not Found"  
nums = [1, 5, 7, 8, 9, 10]
print("Index:", binary_search(nums, 9))
print("Index:", binary_search(nums, 4))

# #output
# PS C:\Users\303379\day4_training> & C:/Users/303379/AppData/Local/Microsoft/WindowsApps/python3.13.exe c:/Users/303379/day4_training/binary_search.py
# Index: 4
# Index: Not Found
# PS C:\Users\303379\day4_training> 
