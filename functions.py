# [EXERCISE] functions
# fizz buzz algorithm

# RULES
# - If the input is divisible by 3, it will return string "Fizz"
# - If the input is divisible by 5, it will return string "Buzz"
# - If the input is divisible by both 3 and 5, it will return string "FizzBuzz"
# - For any other numbers, it will return the same integer input


# def fizz_buzz(input):


# print(fizz_buzz(15))


# SOLUTION:

def fizz_buzz(input):

    if (input % 3 == 0) and (input % 5 == 0):
        return "FizzBuzz"
    if input % 3 == 0:
        return "Fizz"
    if input % 5 == 0:
        return "Buzz"
    return input


print(fizz_buzz(3))
