# scope

# best practice
# - create functions with parameters and local variables

# global variable
message = "a"


def greet(name):

    # local variable
    message = "b"


print(message)

# OUTPUT:
#
# a


# BAD PRACTICE TO AVOID
#
# This might have multiple functions that rely on the value of this global variable
# This might have a side effect in other functions if we accidentally or deliberately changed the value of the  global variable in one function

# message = "a"


# def greet(name):
#     global message
#     message = "b"


# greet("Mosh")
# print(message)
