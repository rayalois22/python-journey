# list unpacking

numbers = [1, 2, 3, 4, 4, 4, 4, 4, 9]
first, *other, last = numbers
print(first, last)
print(other)

# OUTPUT
#
# 1 9
# [2, 3, 4, 4, 4, 4, 4]
