#linear search

def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i  
    return "Not Found"

nums = [10, 7, 8, 9, 1, 5]
print("Index:", linear_search(nums, 9))
print("Index:", linear_search(nums, 2))

#output:
# PS C:\Users\303379\day4_training> & C:/Users/303379/AppData/Local/Microsoft/WindowsApps/python3.13.exe c:/Users/303379/day4_training/linear_search.py
# Index: 3
# Index: Not Found
# PS C:\Users\303379\day4_training> 

