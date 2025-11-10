def partition(arr,low,high):
    i=low-1
    pivot=arr[high]
    for j in range(low,high):
        if pivot>arr[j]:
            i+=1
            arr[j],arr[i]=arr[i],arr[j]
    arr[high],arr[i+1]=arr[i+1],arr[high]
    return i+1
def q_sort(arr,low,high):
    if low<high:
        # high=len(arr)-1
        pi=partition(arr,low,high)

        q_sort(arr,low,pi-1)
        q_sort(arr,pi+1,high)
    return arr


arr=[1,4,3,6,9,7]
print(q_sort(arr,0,len(arr)-1))
