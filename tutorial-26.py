# xargs

# touples
# - iterables
# - iterate over them [means that we can use them in loops]

# def multiply(*numbers):
#     print(numbers)
#
#
# multiply(2, 3, 4, 5)
#
# OUTPUT
#
# (2, 3, 4, 5) - touples


# def multiply(*numbers):
#     total = 1
#     for number in numbers:
#         print(number)
#
#
# multiply(2, 3, 4, 5)
#
# OUTPUT
#
# 2
# 3
# 4
# 5


def multiply(*numbers):
    total = 1
    for number in numbers:
        total *= number
    return total


print(multiply(2, 3, 4, 5))

# OUTPUT
#
# 120
