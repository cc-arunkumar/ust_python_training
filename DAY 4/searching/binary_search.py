list1=[10,20,30,40,50,60,70,80]

num=int(input("Enter Number to Search :"))

low=0; high=len(list1)-1

while low<=high:
    mid=(low+high)//2
    if list1[mid]==num:
        print("Number Found",list1[mid])
        break
    
    elif list1[mid]<num:
        low=mid+1

    else: high=mid-1


# sample output

"""
Enter Number to Search :30
Number Found 30

"""