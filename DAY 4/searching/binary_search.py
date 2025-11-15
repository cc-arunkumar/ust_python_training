list1=[10,20,30,40,50,60,70,80]  # Sorted list for binary search
num=int(input("Enter Number to Search :"))  # Number to search
low=0; high=len(list1)-1  # Initialize low and high indices

while low<=high:
    mid=(low+high)//2  # Middle index
    if list1[mid]==num:  # Check if mid element is the number
        print("Number Found",list1[mid])
        break
    elif list1[mid]<num:  # If mid element less, search right half
        low=mid+1
    else:  # If mid element greater, search left half
        high=mid-1
