#Insertion Sort


def insertionsort(arr):
    n=len(arr)
    if n<=1:
        return
    for i in range(1,n):
        key=arr[i]
        j=i-1
        while j>=0 and key<=arr[j]:
            arr[j+1]=arr[j]
            j-=1
        arr[j+1]=key


arr=[16,14,5,8,1]
insertionsort(arr)
print("Sorted array:",arr)

# #o/p:
# Sorted array: [1, 5, 8, 14, 16]