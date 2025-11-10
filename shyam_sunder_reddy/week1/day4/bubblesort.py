#Bubble sort
list1=[16,14,5,6,8]
print("Before Sorting: ",list1)
for i in range(len(list1)-1):
    swap=True
    for j in range(len(list1)-i-1):
        if list1[j]>list1[j+1]:
            list1[j],list1[j+1]=list1[j+1],list1[j]
            swap=False
    if swap:
        break
print("After Sorting: ",list1)

#Sampel output
# Before Sorting:  [16, 14, 5, 6, 8]
# After Sorting:  [5, 6, 8, 14, 16]