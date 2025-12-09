# Customer Feedback Rating Analyzer

# Task 5: Customer Feedback Rating
# Analyzer

# Scenario:
# Your customer service team collects feedback in a dictionary form
# where key = customer name, value = their rating (out of 5).

# Instructions:
# 1. Create the following dictionary:
# feedback = {"Arjun": 5,"Neha": 4,"Vikram": 3,"Ravi": 4,"Fatima": 5}

# Dictionary Tasks 4
# 2. Add a new feedback: "Priya": 4 .
# 3. Increase Ravi’s rating by 1 (if not already 5).
# 4. Print all customers with a rating of 5.
# 5. Find the average rating of all customers.
# 6. Create a new dictionary using dictionary comprehension to store:
# key = customer name
# value = "Excellent" if rating ≥ 4, else "Needs Improvement" .
# 7. Print the new dictionary.

# Initial feedback dictionary (customer: rating out of 5)
feedback = {"Arjun": 5, "Neha": 4, "Vikram": 3, "Ravi": 4, "Fatima": 5}

# Add new feedback entry
feedback["Priya"] = 4
print(feedback)

# Increase Ravi’s rating by 1 (only if less than 5)
if feedback["Ravi"] < 5:
    feedback["Ravi"] += 1

# Print customers with rating 5
print("Customers with rating 5:")
for customer, rating in feedback.items():
    if rating == 5:
        print(customer)

# Calculate average rating of all customers
average_rating = sum(feedback.values()) / len(feedback)
print(f"\nAverage rating: {average_rating:.2f}")

# Create performance dictionary using comprehension
# "Excellent" if rating >= 4, else "Needs Improvement"
performance = {
    customer: ("Excellent" if rating >= 4 else "Needs Improvement")
    for customer, rating in feedback.items()
}

# Print performance dictionary
print("\nPerformance dictionary:")
print(performance)

#  Output:
# {'Arjun': 5, 'Neha': 4, 'Vikram': 3, 'Ravi': 4, 'Fatima': 5, 'Priya': 4}
# Customers with rating 5:
# Arjun
# Ravi
# Fatima

# Average rating: 4.33