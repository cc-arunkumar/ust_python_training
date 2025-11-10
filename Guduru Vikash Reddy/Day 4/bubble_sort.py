
#Bubble Sort
list = [4, 3, 7, 9, 1]

for i in range(len(list) - 1):
    flag = False
    for j in range(len(list) - i - 1):
        if list[j] > list[j + 1]:
            
            list[j], list[j + 1] = list[j + 1], list[j]
            flag = True
    if not flag:
        break

print("Sorted list:", list)
# # sample output
# Sorted list: [1, 3, 4, 7, 9]
