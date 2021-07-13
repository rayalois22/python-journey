# string methods

course = "  python programming"

# upper case letter / captial letter
course_captial = course.upper()
print(course.upper())

# lower case letter / small letter
print(course.lower())

# title
print(course.title())

# remove the white space which shown from the course variable
print(course.strip())
# left strip
print(course.lstrip())
# right strip
print(course.rstrip())

# find the index of the character
# all the character should be in small letter or else the program will show -1
# return in index
print(course.find("pro"))

# replace a character or a sequence of characters
print(course.replace("p", "j"))

# check for the existance of a character
# return in boolean, True or False
print("pro" in course)

# string does not contain a character or a sequence of characters
# return in boolean, True or False
print("swift" not in course)


# OUTPUT
#
#  PYTHON PROGRAMMING
#  python programming
#  Python Programming
# Python Programming
# Python Programming
#  Python Programming
# 9
# jython jrogramming
# True
# True
