#Employee Feedback System
 
week1 = [4, 3, 5, 4, 2]
week2 = [5, 4, 3, 5, 4]
all_ratings = week1 + week2
total_ratings = len(all_ratings)
average_rating = sum(all_ratings) / total_ratings
print("Total Ratings:", total_ratings)
print("Average Rating:", round(average_rating, 2))
all_ratings.sort()
print("Sorted Ratings:", all_ratings)
filtered = [r for r in all_ratings if r >= 3]
print("Filtered Ratings (above 3):", filtered)
print("Highest:", max(filtered))
print("Lowest:", min(filtered))
final_avg = sum(filtered) / len(filtered)
print("Final Average:", round(final_avg, 2))
 
# Total Ratings: 10
# Average Rating: 3.9
# Sorted Ratings: [2, 3, 3, 4, 4, 4, 4, 5, 5, 5]
# Filtered Ratings (above 3): [3, 3, 4, 4, 4, 4, 5, 5, 5]
# Highest: 5
# Lowest: 3
# Final Average: 4.11