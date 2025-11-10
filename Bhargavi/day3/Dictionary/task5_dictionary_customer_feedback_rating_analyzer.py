# Customer Feedback Rating Analyzer
feedback = {"Arjun": 5,"Neha": 4,"Vikram": 3,"Ravi": 4,"Fatima": 5}

feedback["Priya"] = 4
print(feedback)

if feedback["Ravi"] < 5:
    feedback["Ravi"] += 1

print("Customers with rating 5:")
for customer, rating in feedback.items():
    if rating == 5:
        print(customer)

average_rating = sum(feedback.values()) / len(feedback)
print(f"\nAverage rating: {average_rating:.2f}")

performance = {customer: ("Excellent" if rating >= 4 else "Needs Improvement") for customer, rating in feedback.items()}

print("\nPerformance dictionary:")
print(performance)

# {'Arjun': 5, 'Neha': 4, 'Vikram': 3, 'Ravi': 4, 'Fatima': 5, 'Priya': 4}
# Customers with rating 5:
# Arjun
# Ravi
# Fatima

# Average rating: 4.33