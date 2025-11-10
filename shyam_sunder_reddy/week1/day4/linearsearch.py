#Linear search
l=[10,20,30,40,50,60,70]
key=10
b=True
for i in l:
    if i==key:
        print("Exists in the list")
        b=False
if b:
    print("Does`nt Exists")
    
#Sample output
# Exists in the list