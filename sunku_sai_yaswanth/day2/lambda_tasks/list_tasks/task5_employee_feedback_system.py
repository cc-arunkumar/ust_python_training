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
all_ratings=week1+week2
sum1=sum(all_ratings)
len1=len(all_ratings)
print("Total number of ratings:",len)
avg=sum1/len1
print("Average Rating:",avg)
print("sorted ratings:",sorted(all_ratings))


Filtered_ratings=[]
for rating in all_ratings:
    if rating>3:
        Filtered_ratings.append(rating)

print("Filtered Ratings (above 3):",Filtered_ratings)
print("Highest:",Filtered_ratings[-1])
print("Lowest:",Filtered_ratings[0])
final_average=sum(Filtered_ratings)/len(Filtered_ratings)
print("Final Average:",final_average)





# Average Rating: 3.9
# sorted ratings: [2, 3, 3, 4, 4, 4, 4, 5, 5, 5]
# Filtered Ratings (above 3): [4, 5, 4, 5, 4, 5, 4]
# Highest: 4
# Lowest: 4
# Final Average: 4.428571428571429