# Task 5: Customer Feedback Rating
# Analyzer
# Scenario:
# Your customer service team collects feedback in a dictionary form
# where key = customer name, value = their rating (out of 5).
# Instructions:
# 1. Create the following dictionary:
# feedback = {
#  "Arjun": 5,
#  "Neha": 4,
#  "Vikram": 3,
#  "Ravi": 4,
#  "Fatima": 5
# }
# Dictionary Tasks 4
# 2. Add a new feedback: "Priya": 4 .
# 3. Increase Ravi’s rating by 1 (if not already 5).
# 4. Print all customers with a rating of 5.
# 5. Find the average rating of all customers.
# 6. Create a new dictionary using dictionary comprehension to store:
# key = customer name
# value = "Excellent" if rating ≥ 4, else "Needs Improvement" .
# 7. Print the new dictionary.


feedback = {
    "Arjun": 5,
    "Neha": 4,
    "Vikram": 3,
    "Ravi": 4,
    "Fatima": 5
}

feedback["Priya"] = 4

# Increase Ravi's rating by 1 if less than 5
if feedback["Ravi"] < 5:
    feedback["Ravi"] += 1

# Print customers with rating 5
print("Customers with rating 5:")
for customer, rating in feedback.items():
    if rating == 5:
        print(customer)

# Calculate average rating
average_rating = sum(feedback.values()) / len(feedback)
print("\nAverage Rating:", round(average_rating, 2))

# Create new dictionary with customer status
status_dict = {customer: ("Excellent" if rating >= 4 else "Good") for customer, rating in feedback.items()}

print("\nCustomer Status Dictionary:")
print(status_dict)

# Customers with rating 5:
# Arjun
# Ravi
# Fatima
#
# Average Rating: 4.33
#
# Customer Status Dictionary:
# {'Arjun': 'Excellent', 'Neha': 'Excellent', 'Vikram': 'Good', 'Ravi': 'Excellent', 'Fatima': 'Excellent', 'Priya': 'Excellent'}
