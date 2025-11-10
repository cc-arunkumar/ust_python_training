#Task : Binary Search

#Code
arr=[7,5,4,3,2,]
target=4

def binary_search(arr,target):
    low =0
    high = len(arr)-1

    while(low < high):
        mid = (low + high)//2
        if(arr[mid]==target):
            return mid
        elif arr[mid]< target:
            low= mid+1
        else:
            high=mid-1
    return -1
result = binary_search(arr,target)
print(" Index of target element is at : ",result)

#Output
# Index of target element is at :  2