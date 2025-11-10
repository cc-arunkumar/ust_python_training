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

customers_with_5 = [name for name, rating in feedback.items() if rating == 5]
print("Customers with rating 5:", customers_with_5)

average_rating = sum(feedback.values()) / len(feedback)
print("Average rating:", average_rating)

rating_summary = {name: ("Excellent" if rating >= 4 else "Needs Improvement") for name, rating in feedback.items()}
print(rating_summary)

# ====================sample output=================
# Average rating: 4.333333333333333
# {'Arjun': 'Excellent', 'Neha': 'Excellent', 'Vikram': 'Needs Improvement', 'Ravi': 'Excellent', 'Fatima': 'Excellent', 'Priya': 'Excellent'}
