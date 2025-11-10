# TASK 5 Customer Feedback Rating Analyzer


feedback = {
    "Arjun": 5,
    "Neha": 4,
    "Vikram": 3,
    "Ravi": 4,
    "Fatima": 5
}


feedback["Priya"] = 4


if feedback["Ravi"] < 5:
    feedback["Ravi"] += 1


print("Customers with rating 5:")
for customer, rating in feedback.items():
    if rating == 5:
        print(customer)


total_rating = sum(feedback.values())
average_rating = total_rating / len(feedback)
print("Average rating:", average_rating)

feedback_summary = {customer: ("Excellent" if rating >= 4 else "Needs Improvement") 
                    for customer, rating in feedback.items()}


print("Feedback summary:", feedback_summary)

# -----------------------------------------------------------------------------------

# Sample Output
# Customers with rating 5:
# Arjun
# Ravi
# Fatima
# Average rating: 4.333333333333333
# Feedback summary: {'Arjun': 'Excellent', 'Neha': 'Excellent', 'Vikram': 'Needs Improvement', 'Ravi': 'Excellent', 'Fatima': 'Excellent', 'Priya': 'Excellent'}
