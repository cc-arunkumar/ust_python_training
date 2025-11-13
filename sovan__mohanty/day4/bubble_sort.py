arr=[44,67,23,12,78]
print("Given list: ",arr)
for i in range(len(arr)-1):
    check=False
    for j in range(len(arr)-i-1):
        if(arr[j]>arr[j+1]):
            arr[j],arr[j+1]=arr[j+1],arr[j]
            check=True
    if(check==False):
        break
print("Sorted it using bubble sort",arr)
# #Sample Execution
# Given list:  [44, 67, 23, 12, 78]
# Sorted it using bubble sort [12, 23, 44, 67, 78]