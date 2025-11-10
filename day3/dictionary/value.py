dect={"key":"values"}
a = dict(host="db-server", port=1106)
print(a.keys())
print(a.values())

print(a.items())

product_prices={"apple":190,"banana":120,"mango":200}
print("org price:",product_prices)
# adding value
product_prices["grape"] =60
print("After adding grapes:",product_prices)
# updating existing value
product_prices["banana"]=35
print("after updating prices:",product_prices)

print(product_prices.get("apple"))

kiwi_price = product_prices.get("Kiwi","not found")
print("price of kiwi using get:",kiwi_price)

del product_prices["apple"]
print("After deleting apple:",product_prices)
banana_price = product_prices.pop("banana")
print(banana_price)
print(product_prices)


