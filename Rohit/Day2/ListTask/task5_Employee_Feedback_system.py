# Task 5: Employee Feedback System
# Scenario:
# You are building a small Employee Feedback Portal where employees rate the
# cafeteria food quality each week.
# Step 1: Initialize ratings for two weeks
week1 = [4, 3, 5, 4, 2]
week2 = [5, 4, 3, 5, 4]

# Step 2: Merge week2 ratings into week1 using list's extend method
week1.extend(week2)  # Correct usage: extend is called on the list instance, not the built-in type

# Step 3: Assign the combined ratings to all_ratings
all_ratings = week1

# Step 4: Print the full list of ratings
print(all_ratings)

# Step 5: Calculate and print the total of all ratings
print(sum(all_ratings))

# Step 6: Calculate and print the average rating
print(sum(all_ratings) / len(all_ratings))

# Step 7: Sort the ratings in ascending order
all_ratings.sort()
print(all_ratings)

# Step 8: Filter ratings greater than 3 using a lambda function
filtering = list(filter(lambda x: x > 3, all_ratings))
print("All ratings after filtering", filtering)

# Step 9: Calculate and print the average of filtered ratings
print("Final average after cleaning", sum(filtering) / len(filtering))



# ================sample output=================

# [4, 3, 5, 4, 2, 5, 4, 3, 5, 4]
# 39
# 3.9
# [2, 3, 3, 4, 4, 4, 4, 5, 5, 5]
# All ratings after filtering [4, 4, 4, 4, 5, 5, 5]
# Final average after cleaning 4.428571428571429 