li=[13,56,45,3,2,14,52,1,3,2,4,5,6,7]

for i in range(len(li)-1):
    flag=False
    for j in range(len(li)-i-1):
        if (li[j] > li[j+1]):
            li[j],li[j+1] = li[j+1],li[j]
            flag =True
    if flag==False:
        break 

print(li)


#Sample Output
#[1, 2, 2, 3, 3, 4, 5, 6, 7, 13, 14, 45, 52, 56]