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


n=33426
mean_sum=0
extreme_sum=n%10
n=n//10
while(n>9):
    mean_sum=n%10 + mean_sum
    n=n//10
extreme_sum=extreme_sum+n

if(extreme_sum==extreme_sum):
    print("true")
else:
    print("false")


    

    

