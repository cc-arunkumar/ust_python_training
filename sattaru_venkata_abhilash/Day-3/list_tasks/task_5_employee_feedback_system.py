# Task 5: Employee Feedback System
# Scenario:
# You are building a small Employee Feedback Portal where employees rate cafeteria food quality each week.

# Step 1: Create lists for Week 1 and Week 2 ratings
week1_ratings = [4, 3, 5, 4, 2]
week2_ratings = [5, 4, 3, 5, 4]

# Step 2: Merge both weeks
all_ratings = week1_ratings + week2_ratings

# Step 3: Find total and average rating
total = len(all_ratings)
print("Total Ratings:", total)

average = sum(all_ratings) / total
print("Average Ratings:", round(average, 2))

# Step 4: Sort ratings from lowest to highest
all_ratings.sort()
print("Sorted Ratings:", all_ratings)

# Step 5: Filter out poor ratings (below 3)
good_rating = []
for rating in all_ratings:
    if rating > 3:
        good_rating.append(rating)

# Step 6: Display filtered data
print("Filtered Ratings (above 3):", good_rating)
print("Highest:", good_rating[-1])
print("Lowest:", good_rating[0])

# Step 7: Calculate and print final average
final_average = sum(good_rating) / len(good_rating)
print(f"Final Average: {final_average:.2f}")


# Sample Output:
# Total Ratings: 10
# Average Ratings: 3.9
# Sorted Ratings: [2, 3, 3, 4, 4, 4, 4, 5, 5, 5]
# Filtered Ratings (above 3): [4, 4, 4, 4, 5, 5, 5]
# Highest: 5
# Lowest: 4
# Final Average: 4.43
