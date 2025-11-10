#bubble sort
list1=[5,4,1,7,9]
for i in range(len(list1)):
    is_swap=False
    for j in range(len(list1)-i-1):
        if list1[j]>list1[j+1]:
            list1[j],list1[j+1]=list1[j+1],list1[j]
            is_swap=True
    if is_swap==False:
        break

print(list1)

#sample output
#[1, 4, 5, 7, 9]