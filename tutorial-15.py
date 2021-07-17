# for loops

# range(): use to repeat in specific times like repeat 3 times
# number: variable of type integer

# first way of range
#
# for number in range(3):
#     print("Attempt", number + 1, (number + 1) * ".")
#
# OUTPUT:
#
# Attempt 1 .
# Attempt 2 ..
# Attempt 3 ...

# second way of range
#
# for number in range(1, 4):
#     print("Attempt", number, number * ".")
#
# OUTPUT:
#
# Attempt 1 .
# Attempt 2 ..
# Attempt 3 ...

# third way of range

for number in range(1, 10, 2):
    print("Attempt", number, number * ".")

# OUTPUT:
#
# Attempt 1 .
# Attempt 3 ...
# Attempt 5 .....
# Attempt 7 .......
# Attempt 9 .........
