# debugging

# steps:
# - open debugging panel
# - click settings icon. This will generate a new file called launch.json
# - File path of launch.json: .vscode/launch.json
# - Breakpoint
#   - put the line cursor on a specific line like line 19 and insert by using F9
#   - press F9 one more time to remove the breakpoint
#   - press F5 to run the application up to this point and the specific line is highlighted now
#   - this will automatically opens the integrated terminal
#   - press F10 to execute one statement at a time
#   - press F11 to step into the function if you are calling a function that you have defined
#   - press F10 to see the total
#   - press F10 and you will see that we jump out to the function so the loop did not execute to the completion. That's the reason that our program has a bug
#   - press Shift + F5 to stop the debugger
#   - press Shift + F11 to step out of the specific function without line by line

def multiply(*numbers):
    total = 1
    for number in numbers:
        total *= number
    return total


print("Start")
print(multiply(1, 2, 3))
