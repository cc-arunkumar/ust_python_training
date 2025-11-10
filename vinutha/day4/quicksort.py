#Quick Sort

def quicksort(arr,low,high):
    if low<high:
        pi=partition(arr,low,high)
        quicksort(arr,low,pi-1)
        quicksort(arr,pi+1,high)
def partition(arr,low,high):
    pivot=arr[high]
    i=low-1

    for j in range(low,high):
        if arr[j]<=pivot:
            i+=1
            arr[i],arr[j]=arr[j],arr[i]
    arr[i+1],arr[high]=arr[high],arr[i+1]
    return i+1
arr=[10,7,8,9,1,5]
print("Original array:",arr)
quicksort(arr,0,len(arr)-1)
print("Sorted array:",arr)

#output:
# PS C:\Users\303379\day4_training> & C:/Users/303379/AppData/Local/Microsoft/WindowsApps/python3.13.exe c:/Users/303379/day4_training/quicksort.py
# Original array: [10, 7, 8, 9, 1, 5]
# Sorted array: [1, 5, 7, 8, 9, 10]
# PS C:\Users\303379\day4_training> 
