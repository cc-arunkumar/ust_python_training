#Identify the Even Numbers in a List

ids=eval(input("Enter the Ids"))
even_numbers=list(filter(lambda x: x%2==0,ids))
print(even_numbers)

#Sample Execution
# Enter the Ids[22,43,21,54]
# [22, 54]
