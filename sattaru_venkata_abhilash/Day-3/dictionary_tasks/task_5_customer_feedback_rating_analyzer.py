# Task 5: Customer Feedback Rating Analyzer
# Scenario:
# Your customer service team collects feedback in a dictionary form
# where key = customer name, value = their rating (out of 5).

# Step 1: Create initial dictionary
feedback = {
    "Arjun": 5,
    "Neha": 4,
    "Vikram": 3,
    "Ravi": 4,
    "Fatima": 5
}

# Step 2: Add new feedback
feedback["Priya"] = 4

# Step 3: Increase Ravi's rating by 1 (max 5)
if feedback["Ravi"] < 5:
    feedback["Ravi"] += 1

# Step 4: Print all customers with a rating of 5
print("Customers with rating 5:")
for customer, rating in feedback.items():
    if rating == 5:
        print(customer)

# Step 5: Calculate average rating
average_rating = sum(feedback.values()) / len(feedback)
print("Average Rating:", round(average_rating, 2))

# Step 6: Create new dictionary using comprehension
feedback_summary = {
    customer: ("Excellent" if rating >= 4 else "Needs Improvement")
    for customer, rating in feedback.items()
}

# Step 7: Print the new dictionary
print("Feedback Summary:", feedback_summary)


# Sample Output:
# Customers with rating 5:
# Arjun
# Fatima
# Ravi
# Average Rating: 4.33
# Feedback Summary: {'Arjun': 'Excellent', 'Neha': 'Excellent', 'Vikram': 'Needs Improvement', 'Ravi': 'Excellent', 'Fatima': 'Excellent', 'Priya': 'Excellent'}
