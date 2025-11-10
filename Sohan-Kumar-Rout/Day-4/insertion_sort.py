#Task : Insertion Sort

#Code
arr=[3,90,1,2,34,6]

for i in range(1,len(arr)):
    key = arr[i]
    j=i-1
    while(j>=0 and key < arr[j]):
        arr[j+1]=arr[j]
        j-=1
    arr[j+1]=key
print("Insertion Sort : ",*arr)

#Output
# Insertion Sort :  1 2 3 6 34 90

