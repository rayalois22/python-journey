# types of functions

# 1- Perform a task
# 2- Calculate and return a value

# first form
# lock something to print it in the terminal
# you have to create another function if we want to write that message or send it in an email
# cant reuse this function in any scenarios
def greet(name):
    print(f"Hi {name}")


# second form
# simply returns a value
# we can do whatever we want once we got the value

def get_greeting(name):
    return f"Hi {name}"


message = get_greeting("hezagon")
print(message)

# OUTPUT:
# Hi hezagon

# None: an object that represents the absence of a value
# All functions return none by default unless specifically return a value
# None will not be returned once we return with a string
#
# def greet(name):
#     print(f"Hi {name}")
#
#
# print(greet("Mosh"))
#
# OUTPUT:
# None
