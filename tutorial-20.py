# infinite loops

# program will run forever
while True:
    command = input(">")
    print("ECHO", command)
    # way to jump out from the infinite loop
    if command.lower() == "quit":
        break

# OUTPUT:
#
# >2+2
# ECHO 2+2
# >Quit
# ECHO Quit
