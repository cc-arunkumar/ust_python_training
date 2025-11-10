# Task 5: Employee Feedback System
# Scenario:
# You work on a Sales Dashboard that tracks the daily sales revenue of your
# company’s products.
# Instructions:
# 1. Create a list named sales :
# [1200, 1500, 800, 2200, 1700, 950]
# 2. Calculate and print:
# Total sales for the day
# Average sales per transaction
# (Hint: use sum() and len() )
# 3. Add a new late entry of sale worth 1100 using append() .
# 4. Sort the sales in ascending order and print them.
# Day 3 4
# 5. Display:
# The top 3 highest sales
# The lowest 2 sales
# (Hint: use slicing [-3:] and [:2] )
# 6. Remove the smallest sale from the list and display the updated list.
week1=[4, 3, 5, 4, 2]
week2 = [5, 4, 3, 5, 4]

week1.extend(week2)

all_rating=week1

total_no_of_rating=sum(all_rating)

average_rating = total_no_of_rating/len(all_rating)

print(f"Total no of rating:{total_no_of_rating}")
print(f"Average rating:{average_rating}")

all_rating.sort()

all_rating.pop(0)

print(all_rating)
print(f"Lowest rating:{all_rating[0]}")
print(f"Highest rating:{all_rating[len(all_rating)-1]}")

# EXPECTED OUTPUT:
# PS C:\UST python> & C:/Users/303489/AppData/Local/Programs/Python/Python312/python.exe "c:/UST python/Praveen D/Day 3/Tasks/List/task_11_employee_feedback_system.py"
# Total no of rating:39
# Average rating:3.9
# [3, 3, 4, 4, 4, 4, 5, 5, 5]
# Lowest rating:3
# Highest rating:5