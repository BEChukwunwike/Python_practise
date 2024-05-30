employee = ['Aliyu', 'Bayo', 'Chimezie']
salary = [52000, 43000, 48000]

# Using zip to combine the lists
combined = zip(employee, salary)

# Converting to a list of tuples and printing
employee_salary = list(combined)
print(employee_salary)

# Looping through the zipped tuples
for employee, salary in employee_salary:
    print(employee, salary)
