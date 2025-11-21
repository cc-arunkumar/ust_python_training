list1=[5,8,3,4,1]  # List to sort

for i in range(len(list1)-1):  # Outer loop for passes
    is_sorted=False  # Flag to check if any swap occurs
    for j in range(len(list1)-1-i):  # Inner loop for comparison
        if list1[j]>list1[j+1]:  # Swap if elements are out of order
            list1[j],list1[j+1]=list1[j+1],list1[j]
            is_sorted=True
    if is_sorted==False:  # If no swap in pass, list is sorted
        break

print(list1)  # Print sorted list
 


"""
SAMPLE OUTPUT
[1, 3, 4, 5, 8]

"""