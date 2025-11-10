# insertion sort
list = [3, 6, 1, 2, 8, 5]
n = len(list)

for i in range(n):
    temp = i
    while temp > 0 and list[temp - 1] > list[temp]:
    
        list[temp - 1], list[temp] = list[temp], list[temp - 1]
        temp = temp - 1
print("sorted list", list)
# sample output
# sorted list [1, 2, 3, 5, 6, 8]