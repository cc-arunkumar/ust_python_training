#Linear Search

def linear_search(arr,target):
    for i in range(len(arr)-1):
        if arr[i]==target:
            return i
        else:
            return -1
        
arr=[3,1,6,7,2]
target=2
print(linear_search(arr,target))

#sample output
# 1
