# while loop

# number = 100
# while number > 0:
#     print(number)

#     # number = number // 2
#     number //= 2

# OUTPUT:
#
# 100
# 50
# 25
# 12
# 6
# 3
# 1

command = ""

# lower(): the function will convert the character to lower case when user types in and compare the character with the lower case
while command.lower() != "quit":
    command = input(">")
    print("ECHO", command)

# OUTPUT:
#
# >2 + 2
# ECHO 2 + 2
# >2 + 9
# ECHO 2 + 9
# >Quit
# ECHO Quit
