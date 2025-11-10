ages = [23,67,56,89,34]
categories=list(map(lambda age:'Junior'if age < 30 else 'Mid-level' if age < 45 else 'Senior', ages))

print(categories)
