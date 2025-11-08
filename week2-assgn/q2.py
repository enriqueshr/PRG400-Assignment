# Sample list of employee work hours
work_hours = [35, 42, 38, 45, 50, 39]

# Filter out hours less than 40
filtered_hours = list(filter(lambda hours: hours >= 40, work_hours))

# Convert to overtime hours (hours - 40)
overtime_hours = list(map(lambda hours: hours - 40, filtered_hours))

print("Original hours:", work_hours)
print("Filtered hours (>= 40):", filtered_hours)
print("Overtime hours:", overtime_hours)