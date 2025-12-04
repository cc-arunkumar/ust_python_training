#Task 5: Customer Feedback Rating Analyzer
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
for name in feedback:
    if feedback[name] == 5:
        print(name)

total = 0
count = 0
for rate in feedback.values():
    total += rate
    count += 1
average_rating = total // count
print("Average rating:", average_rating)


result = {}
for name, rating in feedback.items():
    if rating >= 4:
        result[name] = "Excellent"
    else:
        result[name] = "Needs Improvement"

print("New summary:")
for name, status in result.items():
    print(f"{name}: {status}")

'''
output:
Customers with rating 5:
Arjun
Ravi
Fatima
Average rating: 4
New summary:
Arjun: Excellent
Neha: Excellent
Vikram: Needs Improvement
Ravi: Excellent
Fatima: Excellent
Priya: Excellent
'''