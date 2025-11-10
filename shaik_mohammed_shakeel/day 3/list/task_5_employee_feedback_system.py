# Task 5: Employee Feedback System

# Scenario:
# You are building a small Employee Feedback Portal where employees rate the
# cafeteria food quality each week.

# Instructions:
# 1. Create a list of ratings for Week 1:
# week1 = [4, 3, 5, 4, 2]
# (Each number represents feedback given by one employee.)
# 2. Week 2 ratings come in:
# week2 = [5, 4, 3, 5, 4]
# Day 3 5
# Merge both weeks into a list called all_ratings .
# 3. Find:
# The total number of ratings
# The average rating
# (Hint: len() and sum() )
# 4. Sort the ratings from lowest to highest.
# 5. Remove any rating that’s below 3 (filter out poor feedback).
# (Hint: use a loop and create a new list)
# 6. Print:
# All ratings after filtering
# Highest and lowest rating received
# Final average rating after cleaning

week1 = [4, 3, 5, 4, 2]
week2 = [5, 4, 3, 5, 4]
all_ratings=(week1+week2)
print("Total Ratings:",len(all_ratings))
avg=sum(all_ratings)/len(all_ratings)
print("Average Rating: ",avg)
all_ratings.sort()
print("Sorted Ratings: ",all_ratings)
Filtered_ratings=[]
for i in all_ratings:
    if (i>3):
        Filtered_ratings.append(i)
print("Filtered Ratings: ",Filtered_ratings)
print("Highest:",Filtered_ratings[-1])
print("Lowest:",Filtered_ratings[0])
final_avg=sum(Filtered_ratings)/len(Filtered_ratings)
print("Final Average: ",final_avg)

#Sample output
# Total Ratings: 10
# Average Rating:  3.9
# Sorted Ratings:  [2, 3, 3, 4, 4, 4, 4, 5, 5, 5]
# Filtered Ratings:  [4, 4, 4, 4, 5, 5, 5]
# Highest: 5
# Lowest: 4
# Final Average:  4.428571428571429