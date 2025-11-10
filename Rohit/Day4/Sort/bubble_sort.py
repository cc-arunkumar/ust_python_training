array = [5,4,3,2,1]

for i in range(len(array)):
    is_check  =True
    for j in range(len(array)-1-i):
        if array[j]>array[j+1]:
            is_check=False
            array[j],array[j+1] = array[j+1],array[j]
    if is_check:
        break
        


print(array)

# ==========sample output=============
# [1, 2, 3, 4, 5]