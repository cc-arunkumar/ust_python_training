# [5,4,1,7,9]
list=[5,4,1,7,9]

for i in range(len(list)):
    is_swaped=False
    for j in range(len(list)-i-1):
        if list[j]>list[j+1]:
            list[j],list[j+1]=list[j+1],list[j]
            is_swaped=True

    if is_swaped==False:
        break

for i in list:
    print(i)