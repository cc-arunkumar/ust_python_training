#Quick sort

def quick_sort(a):

    if len(a)<=1:

        return a        
    pivot=a[0]
    left=[]
    right=[]
    for i in a[1:]:
        if(i<pivot):
            left.append(i)
        else:
            right.append(i)
    return quick_sort(left)+[pivot]+ quick_sort(right)
        


a=[1,5,3,4,6]
print(quick_sort(a))

#sample output
# [1, 3, 4, 5, 6]
