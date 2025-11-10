list1 = [16, 6, 5, 13, 12, 8, 10]
print("Before Sorting : ", list1)
for i in range(1, len(list1)):
        pivot = list1[i]
        j = i - 1
        while j >= 0 and list1[j] > pivot:
            list1[j + 1] = list1[j]
            j = j - 1
        list1[j + 1] = pivot
print("After Swapping : ", list1)

#Sample Output : 
# Before Sorting :  [16, 6, 5, 13, 12, 8, 10]
# After Swapping :  [5, 6, 8, 10, 12, 13, 16]
