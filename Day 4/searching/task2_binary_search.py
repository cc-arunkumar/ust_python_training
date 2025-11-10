#binary search

list1=[1,2,3,6,7,8,9]

num=int(input("Enter Number to Search :"))

low=0; high=len(list1)-1

while low<=high:
    mid=(low+high)//2
    if list1[mid]==num:
        print("Number is Found",list1[mid])
        break
    
    elif list1[mid]<num:
        low=mid+1

    else: high=mid-1

# sample output:
# Enter Number to Search :3
# Number is Found 3