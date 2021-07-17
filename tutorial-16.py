# for...else


# successful = True

# for number in range(3):
#     print("Attempt")
#     if successful:
#         print("Successful")
#         break
#
# OUTPUT:
#
# Attempt
# Successful


# successful = True

# for number in range(3):
#     print("Attempt")
#     if successful:
#         print("Successful")
#         break
# else:
#     print("Attempted 3 times and failed")
#
# OUTPUT:
#
# Attempt
# Successful


successful = False

for number in range(3):
    print("Attempt")
    if successful:
        print("Successful")
        break
else:
    print("Attempted 3 times and failed")

# OUTPUT:
# Attempt
# Attempt
# Attempt
# Attempted 3 times and failed
