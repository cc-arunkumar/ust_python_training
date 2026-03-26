"""
Scenario:
You are building a small Employee Feedback Portal where employees rate the
cafeteria food quality each week.


"""

# Ratings for week 1
week1=[4,3,5,4,2]

# Ratings for week 2
week2=[5,4,3,5,4]

# Combine ratings from both weeks
all_ratings=week1+week2

# Print total number of ratings
print("Total Ratings:",len(all_ratings))

# Print average rating rounded to 2 decimal places
print("Average Rating:",round(sum(all_ratings)/len(all_ratings),2))

# Sort all ratings in ascending order
all_ratings.sort()

# Print sorted ratings
print("Sorted Ratings:",all_ratings)

# Filter ratings that are 3 or higher
filtered=[r for r in all_ratings if r>=3]

# Print filtered ratings
print("Filtered Ratings (above 3):",filtered)

# Print highest rating from filtered list
print("Highest:",max(filtered))

# Print lowest rating from filtered list
print("Lowest:",min(filtered))

# Print final average of filtered ratings rounded to 2 decimal places
print("Final Average:",round(sum(filtered)/len(filtered),2))


# sample output

"""
Total Ratings: 10
Average Rating: 3.9
Sorted Ratings: [2, 3, 3, 4, 4, 4, 4, 5, 5, 5]
Filtered Ratings (above 3): [3, 3, 4, 4, 4, 4, 5, 5, 5]
Highest: 5
Lowest: 3
Final Average: 4.11

"""
