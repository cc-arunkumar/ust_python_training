list1 = [16, 5, 5, 13, 12, 8]
for i in range(len(list1) - 1):
    is_swapped = False
    for j in range(len(list1) - i - 1):
        if list1[j] > list1[j + 1]:
            list1[j], list1[j+1] = list1[j+1], list1[j]
            is_swapped = True
    if(is_swapped == False):
        break


print(list1)

#Sample Output
#[5, 5, 8, 12, 13, 16]

