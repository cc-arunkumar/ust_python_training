#Task 5: Employee Feedback System

week1 = [4, 3, 5, 4, 2]
week2 = [5, 4, 3, 5, 4]

all_ratings = []
all_ratings = week1+week2

print("Total Ratings: ",len(all_ratings))
print("Average Rating: ",sum(all_ratings)/len(all_ratings))
all_ratings.sort()

new_rating=[]
for i in all_ratings:
    if i>3:
        new_rating.append(i)

print("Filtered Ratings: ",new_rating)
print("Highest: ",max(new_rating))
print("Lowest: ",min(new_rating))
print("Final Average: ",sum(new_rating)/len(new_rating))


#Sample Output
# Total Ratings:  10
# Average Rating:  3.9
# Filtered Ratings:  [4, 4, 4, 4, 5, 5, 5]
# Highest:  5
# Lowest:  4
# Final Average:  4.428571428571429