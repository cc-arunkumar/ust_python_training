n=33426
s1=0
s2=0
c=0
while(n!=0):
    d=n%10
    c+=1
    n=n//10
    if(c==1 or n==0):
        s1=s1+d
    else:
        s2=s2+d
print(s1)
print(s2)
if(s1==s2):
    print("Xylem")
else:
    print("floem")