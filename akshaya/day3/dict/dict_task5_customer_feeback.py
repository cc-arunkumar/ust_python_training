# Task 5: Customer Feedback Rating Analyzer

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

print("Customers with Rating 5:")
for name, rating in feedback.items():
    if rating == 5:
        print(name)


average_rating = sum(feedback.values()) / len(feedback)
print(f"\nAverage Rating: {average_rating:.2f}")

rating_summary = {name: ("Excellent" if rating >= 4 else "Needs Improvement") 
                  for name, rating in feedback.items()}

print("\nRating Summary:")
for name, remark in rating_summary.items():
    print(f"{name}: {remark}")

#sample output
# Customers with Rating 5:
# Arjun
# Ravi
# Fatima

# Average Rating: 4.33

# Rating Summary:
# Arjun: Excellent
# Neha: Excellent
# Vikram: Needs Improvement
# Ravi: Excellent
# Fatima: Excellent
# Priya: Excellent