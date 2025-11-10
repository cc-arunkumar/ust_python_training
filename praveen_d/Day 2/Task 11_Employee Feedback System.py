# Task 5: Employee Feedback System

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