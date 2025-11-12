# Task 5: Customer Feedback Rating
# Analyzer
# Scenario:
# Your customer service team collects feedback in a dictionary form
# where key = customer name, value = their rating (out of 5)


# Step 1: Initialize feedback dictionary with customer names and their ratings
feedback = {
    "Arjun": 5,
    "Neha": 4,
    "Vikram": 3,
    "Ravi": 4,
    "Fatima": 5
}

# Step 2: Add a new customer rating
feedback["Priya"] = 4

# Step 3: Increment Ravi's rating if it's less than 5
if feedback["Ravi"] < 5:
    feedback["Ravi"] += 1  # Ravi's rating becomes 5

# Step 4: Identify customers who gave a rating of 5
customers_with_5 = [name for name, rating in feedback.items() if rating == 5]
print("Customers with rating 5:", customers_with_5)

# Step 5: Calculate average rating across all customers
average_rating = sum(feedback.values()) / len(feedback)
print("Average rating:", average_rating)

# Step 6: Create a summary label for each customer based on their rating
rating_summary = {
    name: ("Excellent" if rating >= 4 else "Needs Improvement")
    for name, rating in feedback.items()
}
print( "showing summary label for each customer based on their rating")
print(rating_summary)

# ====================sample output=================
# Customers with rating 5: ['Arjun', 'Ravi', 'Fatima']
# Average rating: 4.333333333333333
# showing summary label for each customer based on their rating
# {'Arjun': 'Excellent', 'Neha': 'Excellent', 'Vikram': 'Needs Improvement', 'Ravi': 'Excellent', 'Fatima': 'Excellent', 'Priya': 'Excellent'}