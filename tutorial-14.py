# chaining comparison operators

# age should be between 18 and 65
age = 22

# first way to write
if age >= 18 and age < 65:
    print("Eligible")

# second way to write
if 18 <= age < 65:
    print("Eligible")
