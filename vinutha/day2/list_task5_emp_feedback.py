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
# Expected Output(sample):
# Total Ratings: 10
# Average Rating: 3.9
# Sorted Ratings: [2, 3, 3, 4, 4, 4, 4, 5, 5, 5]
# Filtered Ratings (above 3): [4, 4, 4, 4, 5, 5, 5]
# Highest: 5
# Lowest: 4
# Final Average: 4.43

#Code

# Ratings collected for two weeks
week1 = [4, 3, 5, 4, 2]
week2 = [5, 4, 3, 5, 4]

# Combine both weeks' ratings into a single list
all_ratings = week1 + week2

# Print the total number of ratings
print("Total Ratings:", len(all_ratings))

# Calculate and print the average rating (rounded to 2 decimal places)
print("Average Rating:", round(sum(all_ratings)/len(all_ratings), 2))

# Sort the ratings in ascending order
all_ratings.sort()
print("Sorted Ratings:", all_ratings)

# Filter ratings to include only values greater than or equal to 3
filtered = [r for r in all_ratings if r >= 3]
print("Filtered Ratings:", filtered)

# Print the highest rating from the filtered list
print("Highest:", max(filtered))

# Print the lowest rating from the filtered list
print("Lowest:", min(filtered))

# Calculate and print the average of the filtered ratings
print("Final Average:", round(sum(filtered)/len(filtered), 2))



# output
# PS C:\Users\303379\day3_training> & C:/Users/303379/AppData/Local/Microsoft/WindowsApps/python3.13.exe c:/Users/303379/day3_training/task5_emp_feedback.py
# Total Ratings: 10
# Average Rating: 3.9
# Sorted Ratings: [2, 3, 3, 4, 4, 4, 4, 5, 5, 5]
# Filtered Ratings: [3, 3, 4, 4, 4, 4, 5, 5, 5]
# Highest: 5
# Lowest: 3
# Final Average: 4.11
# PS C:\Users\303379\day3_training> 