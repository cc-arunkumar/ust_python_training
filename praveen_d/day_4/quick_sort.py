# [5,6,7,2,4,1]

def quick_sort(list1):
    if len(list1)<=1:
        return list1
    pivot =len(list1)//2

    lower=[]
    equal=[]
    greater=[]

    for i in range(len(list1)):
        if(list1[i]<list1[pivot]):
            lower.append(list1[i])
        elif(list1[i]==list1[pivot]):
            equal.append(list1[i])
        elif(list1[i]>list1[pivot]):
            greater.append(list1[i])

    return quick_sort(lower)+equal+quick_sort(greater)

list1=[5,6,7,2,4,1]

sorted_list=quick_sort(list1)

print(sorted_list)

# EXPECTED OUTPUT
# [1, 2, 4, 5, 6, 7]