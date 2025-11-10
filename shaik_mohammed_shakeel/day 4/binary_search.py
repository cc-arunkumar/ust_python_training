# Binary search

def binary_search(arr,target):
    start=0
    end=len(arr)-1
    target=7
    while start<=end:
        mid=(start+end)//2
        if arr[mid]==target:
            return mid
        elif(arr[mid]<target):
            start=start+1
        else:
            end=end-1
    return -1
arr=[4,5,6,7,9]
target=7
print(binary_search(arr,target))


#sample Output
#3