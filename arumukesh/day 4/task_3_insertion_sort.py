def insert_sort(arr):
    for key in range(1,len(arr)):
        i=key-1
        temp=arr[key]
        while(i>=0  and arr[i]>temp):
            arr[i+1]=arr[i]
            i-=1

        arr[i+1]=temp
    return arr

l=[23,54,34,5,6,1]
print(insert_sort(l))