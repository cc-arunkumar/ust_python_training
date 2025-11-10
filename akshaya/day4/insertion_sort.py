#insertion sort
list1 = [16, 14, 5, 6, 8]

for i in range(1, len(list1)):         
    key = list1[i]                   
    j = i - 1                          

    while j >= 0 and key < list1[j]:  
        list1[j + 1] = list1[j]
        j -= 1                        

    list1[j + 1] = key                

print("Sorted list:", list1)
# sample output
# Sorted list: [5, 6, 8, 14, 16]
