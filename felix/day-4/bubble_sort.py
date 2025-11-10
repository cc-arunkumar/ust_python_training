# bubble_sort


list1 = [4,3,5,7,8,34,56,90,76]
print(f"Initial array: {list1}")

for i in range(len(list1)):
    flag = False
    for j in range(len(list1)-1-i):
        if list1[j] > list1[j+1]:
            list1[j],list1[j+1] = list1[j+1],list1[j]
    if flag == False:
        break
       
print(f"Sorted array: {list1}")

# output

# Initial array: [4, 3, 5, 7, 8, 34, 56, 90, 76]
# Sorted array: [3, 4, 5, 7, 8, 34, 56, 76, 90]