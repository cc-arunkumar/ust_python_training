

# while(True):
#     choice = int(input("Enter choice: "))
#     match choice:
#         case 1:
#             print("hello 1")
#         case 2:
#             print("hello 2")
#         case 3:
#             print("hello 3")
#         case 4:
#             break

for i in range(10):
    for j in range(10):
        if i<5 and i+j>=6 and j-i<=4:
            print("*",end="")
        elif i>=5 and i-j<=4 and i+j<=14:
            print("*",end="")
        else:
            print(" ",end="")
    print()
    
print("Butterfly")
for i in range(10):
    for j in range(10):
        if i<5 and i<=j and i+j<=9:
            print("*",end="")
        elif i>=5 and i+j>=9 and j<=i:
            print("*",end="")
        else:
            print(" ",end="")
    print()

print("----X----")
for i in range(5):
    for j in range(5):
        if i==j or i+j==4:
            print("*",end="")
        else:
            print(" ",end="")
    print()
    
print("----u----")
for i in range(5):
    for j in range(5):
        if j==0 or j==4 or i==4:
            print("*",end="")
        else:
            print(" ",end="")
    print()
    
print("----+----")
for i in range(5):
    for j in range(5):
        if j==2 or i==2:
            print("*",end="")
        else:
            print(" ",end="")
    print()
    
#   0 1 2 3 4 5 6 7 8 9
# 1 *                *  
# 2   *           *
# 3     *       *
# 4       *   *
# 5         *
# 6       *   *
# 7     *       *
# 8   *           *
# 9 * * * * * * * * * 