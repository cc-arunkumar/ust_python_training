l=[1,2,3,4,5,6,7,8,9,10]
key=7
b=True
for i in l:
    if i==key:
        print("Exists in the list at:",i)
        b=False
if b:
    print("Does`nt Exists")
    
#output
#Exists in the list at: 7