# n = int(input("Enter the number"))
# n=124

# first = 0
# second =1
# sum=0
# for i in range(2,n):
    
#     sum= first+second
#     first=second
#     second=sum

# print(sum)

# if n%10==7 or n%7==0:
#     print("Buzz")
    
# print(n//10)

# n = 175
# temp = n
# count=0
# while(temp>0):
#     n=n//10
#     count+=1
# sum=0
# while( n>0):
#     val=n%10
#     sum=sum+val**count
#     count-=1
#     n=n//10

# print(sum)

# n = 175
# temp = n
# count = 0

# while temp > 0:
#     temp = temp // 10
#     count += 1

# sum = 0
# temp = n  
# while temp > 0:
#     digit = temp % 10
#     sum += digit ** count
#     temp = temp // 10
#     count-=1

# print(sum)

# n =1221

# temp=n*2
# print(temp)
# count=0
# val1=0
# val2=0
# while temp>0:
#     if(count==1):
#         val1= n%10
#     if(count==2):
#         val2=n%10
#     temp=temp//10
#     count+=1
# if val1==val2:
#     print(True)



# n = 13569
# previous =n%10
# n=n//10
# temp = n
# current =0
# while temp>0:
#     current = temp%10
#     if current>previous:
#         break
#     previous = current
#     temp = temp//10

# if temp==0:
#     print(True)
# else:
#     print(False)
    
# n = 875213
# previous =n%10
# n=n//10
# temp = n
# current =0
# while temp>0:
#     current = temp%10
#     if current<previous:
#         break
#     previous = current
#     temp = temp//10

# if temp==0:
#     print(True)
# else:
#     print(False)

# def is_bouncing(number):
#     digits = list(str(number))
#     increasing = decreasing = True

#     for i in range(1, len(digits)):
#         if digits[i] > digits[i - 1]:
#             decreasing = False
#         elif digits[i] < digits[i - 1]:
#             increasing = False

#     return not (increasing or decreasing)

# num = 945216
# if is_bouncing(num):
#     print(f"{num} is a bouncing number.")
# else:
#     print(f"{num} is not a bouncing number.")

    
    
    
n = 121


# first_digit = int(str(n)[0])
# val = n%10
# sum = first_digit+val
# temp = n//10
# sum1=0
# while(temp>0):
#     val2 = temp%10
#     sum1+=val2
#     temp =temp//10
# sum1 = sum1-first_digit

# if(sum==sum1):
#     print(True)


    
