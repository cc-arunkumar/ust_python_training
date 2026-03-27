#Employee Feedback System

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

# Ratings collected for two weeks
week1 = [4, 3, 5, 4, 2]
week2 = [5, 4, 3, 5, 4]

# Combine both weeks' ratings
all_ratings = week1 + week2

# Calculate total number of ratings
total_ratings = len(all_ratings)
print("Total Ratings:", total_ratings)

# Calculate average rating across all ratings
average_rating = sum(all_ratings) / total_ratings
print("Average Rating:", round(average_rating, 2))

# Sort ratings in ascending order
all_ratings.sort()
print("Sorted Ratings:", all_ratings)

# Filter ratings that are greater than or equal to 3
filtered = [r for r in all_ratings if r >= 3]
print("Filtered Ratings (above 3):", filtered)

# Find highest rating from filtered list
print("Highest:", max(filtered))

# Find lowest rating from filtered list
print("Lowest:", min(filtered))

# Calculate average of filtered ratings
final_avg = sum(filtered) / len(filtered)
print("Final Average:", round(final_avg, 2))

#  Output:
# Total Ratings: 10
# Average Rating: 3.9
# Sorted Ratings: [2, 3, 3, 4, 4, 4, 4, 5, 5, 5]
# Filtered Ratings (above 3): [3, 3, 4, 4, 4, 4, 5, 5, 5]
# Highest: 5
# Lowest: 3
# Final Average: 4.11
