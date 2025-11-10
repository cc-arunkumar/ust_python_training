# #Task 5: Employee Feedback System
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
week1.extend(week2)
all_rating=week1
print("Total Ratings: ",len(all_rating))
print("Average Rating: ",sum(all_rating)/len(all_rating))
all_rating.sort()
print("Sorted Ratings: ",all_rating)
all_rating=list(filter(lambda x:x>3,all_rating))
print("Filtered Ratings (above 3): ",all_rating)
print("Highest: ",all_rating[0])
print("Lowest: ",all_rating[len(all_rating)-1])
print("Final Average: ",sum(all_rating)/len(all_rating))

#Sample output
# Total Ratings:  10
# Average Rating:  3.9
# Sorted Ratings:  [2, 3, 3, 4, 4, 4, 4, 5, 5, 5]     
# Filtered Ratings (above 3):  [4, 4, 4, 4, 5, 5, 5]  
# Highest:  4
# Lowest:  5
# Final Average:  4.428571428571429