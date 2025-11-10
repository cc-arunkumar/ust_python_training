#bubble sort

list = [1,2,5,3,6]

for i in range(len(list)-1):
    flag = False
    for j in range(len(list)-i-1):
        if(list[j]>list[j+1]):
            list[j],list[j+1]=list[j+1],list[j]
            flag = True
    if(flag==False):
                break
print("The sorted list is:",list)

# sample output :
# [1, 2, 3, 5, 6]