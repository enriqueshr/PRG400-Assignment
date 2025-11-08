# Sample list of product prices
product_prices = [45.0, 55.0, 30.0, 70.0, 25.0, 60.0]

# Filter out prices below $50
filtered_prices = list(filter(lambda price: price >= 50, product_prices))

# Apply 10% discount to the remaining prices
discounted_prices = list(map(lambda price: price * 0.9, filtered_prices))

print("Original prices:", product_prices)
print("Filtered prices (>= $50):", filtered_prices)
print("Discounted prices (10% off):", discounted_prices)