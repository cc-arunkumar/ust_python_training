# n = 13569
# is_increasing = True
# previous = -1 
# while n > 0:
#     digit = n % 10
#     if digit >= previous and previous != -1:
#         is_increasing = False
#         break
#     previous = digit
#     n = n // 10

# if is_increasing:
#     print("true.")
# else:
#     print("false")


n=1234
rev=0
while n>0:
    digit=n%10
    rev=rev*10+digit
    n=n//10

print(rev)


s="hello world"
words=s.split()
rev=[]
for w in words:
    rev.append(w[::-1])
    
res=" ".join(rev)
print(res)

    

    

