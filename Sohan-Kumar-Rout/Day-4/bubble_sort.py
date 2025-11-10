#Task : Bubble Sort 

#Code
arr=[3,90,1,2,34,6]
for i in range(len(arr)-1):
    for j in range(len(arr) -i-1):
        if(arr[j] > arr[j+1]):
            arr[j],arr[j+1]=arr[j+1],arr[j]
print("Bubble Sort : ",*arr)

#Output
# Bubble Sort :  1 2 3 6 34 90