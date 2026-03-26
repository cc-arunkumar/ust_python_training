list1=[4,7,3,5,1]  # List to sort

for i in range(1,len(list1)):  # Start from second element
    key=list1[i]  # Current element to insert
    j=i-1  # Index of previous element

    while j>=0 and key<list1[j]:  # Shift elements greater than key to right
        list1[j+1]=list1[j]
        j=j-1
    
    list1[j+1]=key  # Insert key at correct position

print(list1)  # Print sorted list

"""
SAMPLE OUTPUT

[1, 3, 4, 5, 7]

"""