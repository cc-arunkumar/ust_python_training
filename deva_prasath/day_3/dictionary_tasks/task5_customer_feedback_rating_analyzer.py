# customer_feedback_rating_analyzer.py
# Your customer service team collects feedback in a dictionary form
# where key = customer name, value = their rating (out of 5)

# Dictionary storing feedback ratings for customers
feedback = {
    "Arjun": 5,
    "Neha": 4,
    "Vikram": 3,
    "Ravi": 4,
    "Fatima": 5
}

# Add new customer (Priya) with a rating of 4
feedback['Priya'] = 4
print("After Priya addition: ", feedback)

# Update Ravi's feedback to 5 if it's not already 5
for key, val in feedback.items():
    if key == "Ravi" and val != 5:
        feedback[key] = 5

# Print customers who have a rating of 5
for key, val in feedback.items():
    if val == 5:
        print("Customers with rating of 5: ", key)

# Calculate the average feedback rating
sumi = 0
for val in feedback.values():
    sumi += val
avg = sumi // len(feedback)  # Use integer division for average
print("Average rating: ", avg)

# Create a new dictionary to classify feedback
new_dict = {}
for key, val in feedback.items():
    if val >= 4:
        new_dict[key] = "Excellent"  # If rating is 4 or higher, mark as Excellent
    else:
        new_dict[key] = "Needs Improvement"  # Otherwise, mark as Needs Improvement

# Print the final classification of feedback
print("Final dict:", new_dict)


#Sample output

# After Priya addition:  {'Arjun': 5, 'Neha': 4, 'Vikram': 3, 'Ravi': 4, 'Fatima': 5, 'Priya': 4}
# Customers with  rating of 5:  Arjun
# Customers with  rating of 5:  Ravi
# Customers with  rating of 5:  Fatima
# Average rating:  4
# 4
# Final dict: {'Arjun': 'Excellent', 'Neha': 'Excellent', 'Vikram': 'Needs Improvement', 'Ravi': 'Excellent', 'Fatima': 'Excellent', 'Priya': 'Excellent'}