# task 1:
# Take input from ennd user for  marks of 5 subj
# cal total and percentage
# A -> 90 and above
# B -> 80-89
# C -> 70-79
# D -> 60-69
# E -> below 60

sub1 = int(input("enter marks of maths "))
sub2 = int(input("enter marks of sst "))
sub3 = int(input("enter marks of science "))
sub4 = int(input("enter marks of english "))
sub5 = int(input("enter marks of hindi "))
total = (sub1 + sub2 + sub3 + sub4 +sub5)
print(total)
percentage = (total/500) * 100
print(percentage)

if(percentage >= 90):
    print("A")
elif(percentage<=89 and percentage >=80):
    print("B")
elif(percentage<=79 and percentage >=70):
    print("C")
elif(percentage<=69 and percentage >=60):
    print("D")
# if(percentage<=60):
else:
    print("F")


  
   
