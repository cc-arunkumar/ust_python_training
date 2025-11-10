arr=[5,4,1,7,9]
for i in range(len(arr)):
    flag=False
    for j in range(len(arr)-i-1):
        if arr[j]>arr[j+1]:
            arr[j],arr[j+1]=arr[j+1],arr[j]
            flag=True
    if flag==False:
        print(arr)
        break

for i in arr:
    print(i,end=" ")