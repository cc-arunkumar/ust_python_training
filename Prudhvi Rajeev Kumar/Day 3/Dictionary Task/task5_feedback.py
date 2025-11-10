feedback = {
 "Arjun": 5,
 "Neha": 4,
 "Vikram": 3,
 "Ravi": 4,
 "Fatima": 5
}

feedback["Priya"] = 4
feedback["Ravi"] += 1 if feedback["Ravi"] != 5 else ""

for name, rating in feedback.items():
    if rating == 5:
        print(name)


total_rating = sum(feedback.values())
count = len(feedback)
average = total_rating/count
print(average)


status_dict = {name: ("Excellent" if rating >= 4 else "Needs Improvement") for name, rating in feedback.items()}
print(status_dict)

