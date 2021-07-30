# xxargs

# we can pass multiple key value pairs or multiple key word arguments when using double asterisks

def save_user(**user):
    # print the value of various keys in this dictionary
    print(user["name"])


save_user(id=1, name="John", age="22")

# OUTPUT:
#
# {'id': 1, 'name': 'John', 'age': '22'} - Dictionary
