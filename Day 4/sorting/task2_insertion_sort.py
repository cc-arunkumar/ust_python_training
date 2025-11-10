#insertion sort

list1=[3,4,15,6,17,8]

for i in range(1,len(list1)):
    key=list1[i]
    j=i-1

    while j>=0 and key<list1[j]:
        list1[j+1]=list1[j]
        j=j-1
    
    list1[j+1]=key

print(list1)

# sample output:
# [3, 4, 6, 8, 15, 17]