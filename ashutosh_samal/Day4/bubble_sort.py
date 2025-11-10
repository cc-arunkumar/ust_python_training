list1=[16,14,5,6,8]

for i in range(len(list1)-1):
    is_swap = False
    for j in range(len(list1)-i-1):
        if list1[j]>list1[j+1]:
            list1[j],list1[j+1]=list1[j+1],list1[i]
            is_swap = True
    if(is_swap==False):
        break
    
print(list1)

#Sample Execution
#[5, 5, 6, 8, 14]