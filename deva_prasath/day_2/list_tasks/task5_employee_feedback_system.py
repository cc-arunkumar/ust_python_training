#Employee Feedback System
# You are building a small Employee Feedback Portal where employees rate the
# cafeteria food quality each week.

# Ratings for week 1 and week 2
week1 = [4, 3, 5, 4, 2]
week2 = [5, 4, 3, 5, 4]

# Combine ratings from both weeks
all_ratings = week1 + week2

# Print the total number of ratings
print("Total ratings:", len(all_ratings))

# Calculate and print the average rating
print("Average ratings: ", sum(all_ratings) / len(all_ratings))

# Sort the ratings in ascending order
all_ratings.sort()
print("Sorted ratings: ", all_ratings)

# Filter ratings above 3
filterd_list = []
for i in all_ratings:
    if i > 3:
        filterd_list.append(i)
print("Filtered rating (above 3): ", filterd_list)

# Print the highest and lowest ratings
print("Highest:", max(all_ratings))
print("Lowest:", min(all_ratings))

# Calculate and print the final average of filtered ratings
fin_avg = sum(filterd_list) / len(filterd_list)
print("Final Average:", round(fin_avg, 2))


#Sample output

# Total ratings: 10
# Average ratings:  3.9
# Sorted ratings:  [2, 3, 3, 4, 4, 4, 4, 5, 5, 5]
# Filtered rating(above 3):  [4, 4, 4, 4, 5, 5, 5]
# Highest: 5
# Lowest: 2
# Final Average: 4.43

