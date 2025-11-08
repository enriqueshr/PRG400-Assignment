# Sample list of customer feedback strings
feedbacks = ["This product is amazing!", "Bad quality.", "I love it, highly recommend!", "Too expensive.", "Great value for money and excellent service."]

# Filter out messages shorter than 20 characters
filtered_feedbacks = list(filter(lambda msg: len(msg) >= 20, feedbacks))

# Convert remaining messages to lowercase
lowercase_feedbacks = list(map(lambda msg: msg.lower(), filtered_feedbacks))

print("Original feedbacks:", feedbacks)
print("Filtered feedbacks (>= 20 chars):", filtered_feedbacks)
print("Lowercase feedbacks:", lowercase_feedbacks)