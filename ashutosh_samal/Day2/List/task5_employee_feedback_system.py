#Task 5: Employee Feedback System

# Ratings for Week 1 and Week 2
week1 = [4, 3, 5, 4, 2]
week2 = [5, 4, 3, 5, 4]

# Combining the ratings from both weeks into a single list
all_ratings = week1 + week2

# Printing the total number of ratings by calculating the length of the combined list
print("Total Ratings: ", len(all_ratings))

# Calculating and printing the average rating by dividing the sum by the number of ratings
print("Average Rating: ", sum(all_ratings) / len(all_ratings))

# Sorting the ratings in ascending order
all_ratings.sort()

# Filtering out ratings that are greater than 3 using a for loop
new_rating = []
for i in all_ratings:
    if i > 3:
        new_rating.append(i)

# Printing the filtered list of ratings (those greater than 3)
print("Filtered Ratings: ", new_rating)

# Printing the highest and lowest rating from the filtered list
print("Highest: ", max(new_rating))
print("Lowest: ", min(new_rating))

# Calculating and printing the average of the filtered ratings
print("Final Average: ", sum(new_rating) / len(new_rating))



#Sample Output
# Total Ratings:  10
# Average Rating:  3.9
# Filtered Ratings:  [4, 4, 4, 4, 5, 5, 5]
# Highest:  5
# Lowest:  4
# Final Average:  4.428571428571429