array = [1,2,3,4,5,6,7,8]
target = 3
start = 0
end = len(array)-1
while(start<=end):
    mid = (start+end)//2
    # print(mid)
    if array[mid]==target:
        print(f"numbers is found at index {mid}")
        break
    elif array[mid]>target:
        end=mid-1
    else:
        start=mid+1
        
# ==========sample output=============
# numbers is found at index 2