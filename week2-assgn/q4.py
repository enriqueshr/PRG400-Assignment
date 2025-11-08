# Sample dictionary of employee names and salaries
employee_salaries = {"Alice": 55000, "Bob": 65000, "Charlie": 58000, "David": 70000, "Eve": 62000}

# Filter out employees with salaries less than $60,000
filtered_employees = dict(filter(lambda item: item[1] >= 60000, employee_salaries.items()))

# Apply 5% raise to remaining salaries
raised_salaries = dict(map(lambda item: (item[0], item[1] * 1.05), filtered_employees.items()))

print("Original salaries:", employee_salaries)
print("Filtered employees (>= $60,000):", filtered_employees)
print("Raised salaries (5%):", raised_salaries)