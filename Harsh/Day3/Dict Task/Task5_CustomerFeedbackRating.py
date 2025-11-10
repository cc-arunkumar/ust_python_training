
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

average_rating = sum(feedback.values()) / len(feedback)
print("\nAverage Rating:", round(average_rating, 2))

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
