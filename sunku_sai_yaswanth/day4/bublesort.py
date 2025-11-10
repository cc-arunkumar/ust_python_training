# --------------------Bublesort-------------------
numbers=[16,14,5,6,8]
for i in range(len(numbers)-1):
    bool==False
    for j in range(len(numbers)-i-1):
        if numbers[j]>numbers[j+1]:
            numbers[j],numbers[j+1]=numbers[j+1],numbers[j]

            bool==True
            if(bool==False):
                break
print("buble sort:",numbers)

# output
# buble sort: [5, 6, 8, 14, 16]


