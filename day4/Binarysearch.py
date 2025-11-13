binary=[1,3,5,6,8,9,12,15]
target=12
start=0
end=len(binary)-1
while start<=end:
    mid=(start+end)//2
    if binary[mid]==target:
        
        print(f"the target is found at index {mid}")
        break
    elif target>binary[mid]:
        start=mid+1
    else:
        end=mid-1
else:
    print("element is not found")

# output
# the target is found at index 6