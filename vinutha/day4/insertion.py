#insertion sort:

arr=[5,3,6,2,9,1]
for i in range(1,len(arr)):
    for j in range(i,0,-1):
        if arr[j]<arr[j-1]:
            arr[j],arr[j-1]=arr[j-1],arr[j]
        else:
            break
print("Sorted:",arr)

#output:
# PS C:\Users\303379\day4_training> & C:/Users/303379/AppData/Local/Microsoft/WindowsApps/python3.13.exe c:/Users/303379/day4_training/insertion.py
# Sorted: [1, 2, 3, 5, 6, 9]
# PS C:\Users\303379\day4_training> 