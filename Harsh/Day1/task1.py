sub1=int(input("Enter the first sub: "))
sub2=int(input("Enter the second sub: "))
sub3=int(input("Enter the third sub: "))
sub4=int(input("Enter the fourth sub: "))
sub5=int(input("Enter the fifth sub: "))

total=(sub1+sub2+sub3+sub4+sub5)
percent=(total/500)*100
print(f"total: {total} , percentage: {percent}" )
if(percent>=90):
    print("A")
elif(percent<=80 and percent>=89 ):
    print("B")
elif(percent<=70 and percent>=79 ):
    print("C")
elif(percent<=60 and percent>=69 ):
    print("D")
else:
    print("F")
