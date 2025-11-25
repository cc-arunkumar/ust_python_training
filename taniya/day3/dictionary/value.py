# Simple dictionary
dect = {"key": "values"}

# Create dictionary using dict() constructor
a = dict(host="db-server", port=1106)

# Print dictionary keys
print(a.keys())

# Print dictionary values
print(a.values())

# Print dictionary items (key-value pairs)
print(a.items())

# Product prices dictionary
product_prices = {"apple": 190, "banana": 120, "mango": 200}
print("org price:", product_prices)

# Adding a new key-value pair
product_prices["grape"] = 60
print("After adding grapes:", product_prices)

# Updating existing value
product_prices["banana"] = 35
print("after updating prices:", product_prices)

# Access value using get()
print(product_prices.get("apple"))

# Access non-existing key using get() with default value
kiwi_price = product_prices.get("Kiwi", "not found")
print("price of kiwi using get:", kiwi_price)

# Delete a key-value pair using del
del product_prices["apple"]
print("After deleting apple:", product_prices)

# Remove and return value using pop()
banana_price = product_prices.pop("banana")
print(banana_price)
print(product_prices)

# -------------------------
# Expected Output:
# dict_keys(['host', 'port'])
# dict_values(['db-server', 1106])
# dict_items([('host', 'db-server'), ('port', 1106)])
# org price: {'apple': 190, 'banana': 120, 'mango': 200}
# After adding grapes: {'apple': 190, 'banana': 120, 'mango': 200, 'grape': 60}
# after updating prices: {'apple': 190, 'banana': 35, 'mango': 200, 'grape': 60}
# 190
# price of kiwi using get: not found
# After deleting apple: {'banana': 35, 'mango': 200, 'grape': 60}
# 35
# {'mango': 200, 'grape': 60}