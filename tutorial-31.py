# lists

letters = ["a", "b", "c"]
matrix = [[0, 1], [2, 3]]

# different ways to create a list
zeros = [0] * 5
print(zeros)

# OUTPUT
#
# [0, 0, 0, 0, 0]


# COMBINED

combined = zeros + letters
print(combined)

# OUTPUT
#
# [0, 0, 0, 0, 0, 'a', 'b', 'c']


# NUMBERS

numbers = list(range(20))
print(numbers)

# OUTPUT
#
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19]


# CHARACTERS

chars = list("Hello World")
print(chars)

# OUTPUT
#
# ['H', 'e', 'l', 'l', 'o', ' ', 'W', 'o', 'r', 'l', 'd']
