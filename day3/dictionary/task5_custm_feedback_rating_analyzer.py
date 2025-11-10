feedback = {"Arjun": 5, "Neha": 3, "Ravi": 4, "Fatima": 5}

feedback["Priya"] = 4
feedback["Ravi"] += 1 if feedback["Ravi"] < 5 else 0

print([name for name, rate in feedback.items() if rate == 5])
print(sum(feedback.values()) / len(feedback))

result = {n: ("Excellent" if r >= 4 else "Needs Improvement") for n, r in feedback.items()}
print(result)
