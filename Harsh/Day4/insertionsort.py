
def insertion_sort(arr):
    for i in range(1,len(arr)):
        temp=arr[i]
        j=i-1
        while(j>=0 and arr[j]>temp):
            arr[j+1]=arr[j]
            j-=1
        arr[j+1]=temp
        

arr=[5,2,3,4,8,6,8,0,1,3]
print("Unsorted arr:", arr)
insertion_sort(arr)
print("sorted arr:", arr)

# Unsorted arr: [5, 2, 3, 4, 8, 6, 8, 0, 1, 3]
# sorted arr: [0, 1, 2, 3, 3, 4, 5, 6, 8, 8]