#Task 5: Employee Feedback System

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

week1 = [4, 3, 5, 4, 2]
week2 = [5, 4, 3, 5, 4]

all_ratings = week1+week2
total_no_of_ratings = len(all_ratings)
print("Total Ratings:", total_no_of_ratings)
average_rating = sum(all_ratings)/total_no_of_ratings 
print("Average Rating:", average_rating)  
sorted_ratings = sorted(all_ratings)
print("Sorted Ratings:", sorted_ratings)
filtered_ratings = []
for rating in sorted_ratings:
    if rating >3:
        filtered_ratings.append(rating)
print("Filtered Ratings (above 3):", filtered_ratings)
highest_rating = max(filtered_ratings)
lowest_rating = min(filtered_ratings)
final_average_rating = sum(filtered_ratings)/len(filtered_ratings)
print("Highest Rating:", highest_rating)
print("Lowest Rating:", lowest_rating)
print("Final Average Rating:", final_average_rating)

#Sample 
# Total Ratings: 10
# Average Rating: 3.9
# Sorted Ratings: [2, 3, 3, 4, 4, 4, 4, 5, 5, 5]
# Filtered Ratings (above 3): [4, 4, 4, 4, 5, 5, 5]
# Highest Rating: 5
# Lowest Rating: 4
# Final Average Rating: 4.428571428571429