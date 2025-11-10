arr = [5,4,3,2,1]


for i in range(0, len(arr)):
    key = arr[i]         
    j = i - 1           
    while j >= 0 and arr[j] >key:
        arr[j + 1]= arr[j]
        j-= 1
    arr[j + 1]= key     
        
print(arr)

# ==========sample output=============
# [1, 2, 3, 4, 5]