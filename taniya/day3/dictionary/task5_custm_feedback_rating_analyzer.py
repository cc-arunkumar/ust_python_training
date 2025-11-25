# Initial feedback dictionary with employee ratings
feedback = {"Arjun": 5, "Neha": 3, "Ravi": 4, "Fatima": 5}

# Add a new employee's feedback
feedback["Priya"] = 4

# Increase Ravi's rating by 1 only if it's less than 5
feedback["Ravi"] += 1 if feedback["Ravi"] < 5 else 0

# Print all employees who have a rating of 5
print([name for name, rate in feedback.items() if rate == 5])

# Calculate and print average rating
print(sum(feedback.values()) / len(feedback))

# Create a result dictionary with performance remarks
result = {n: ("Excellent" if r >= 4 else "Needs Improvement") for n, r in feedback.items()}
print(result)

# -------------------------
# Expected Output:
# ['Arjun', 'Fatima', 'Ravi']
# 4.2
# {'Arjun': 'Excellent', 'Neha': 'Needs Improvement', 'Ravi': 'Excellent', 'Fatima': 'Excellent', 'Priya': 'Excellent'}