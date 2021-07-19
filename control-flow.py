# exercises

# OUTPUT:
# 2
# 4
# 6
# 8
# We have 4 even numbers
# HINT: USE range(1, 10)
#
# ANSWER:
#
count = 0

for numbers in range(1, 10):
    if numbers % 2 == 0:
        count += 1
        print(numbers)
print(f"We have {count} even numbers")


# hezagon's answer
#
# for numbers in range(1, 10):
#     print(numbers * 2)
# else:
#     print("We have", numbers, "even numbers")
#
# OUTPUT:
#
# 2
# 4
# 6
# 8
# 10
# 12
# 14
# 16
# 18
# We have 9 even numbers
