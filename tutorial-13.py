# short-circuit evaluation
#
# logical operator are the short-circuit
# Python will evaluate the statement from the first variable
# if the first variable is false, the result will get false even the second variable and third variables are true

high_income = True
good_credit = True
student = True

if high_income or good_credit and not student:
    print("Eligible")
