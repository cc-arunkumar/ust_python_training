lis1 = [16,14,5,6,8]
for i in range(len(lis1) - 1):
    check = False
    for j in range(len(lis1)-i-1):
        if(lis1[j] > lis1[j+1]):
            lis1[j],lis1[j+1]=lis1[j+1],lis1[j]
            check = True
    if check == False:
     break
print("Sorted list(bubble sort)",lis1)

