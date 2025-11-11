# Binary Search

arr=[23,24,45,54,66]
target=54
start=0
end=len(arr)-1

while(start<=end):
    mid=(start+end)//2
    if(target==arr[mid]):
        print("The target index in the array:",mid)
        break
    elif(target>arr[mid]):
        start=mid+1
    else:
        end=mid-1
else:
    print("Index not found")
    
# Sample output
# The target index in the array: 3