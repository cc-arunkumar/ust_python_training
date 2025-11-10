#insertion sort

arr=[10,4,7,18,1,2]
for i in range (1,len(arr)):
    for j in range (i,0,-1):
        if arr[j]<arr[j-1]:
            arr[j],arr[j-1]=arr[j-1],arr[j]
        else:
            break
print("sorted:",arr)

#insertionsort
#sorted: [1, 2, 4, 7, 10, 18]