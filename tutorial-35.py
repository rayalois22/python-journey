# adding or removing items

letters = ["a", "b", "c"]

# Add
#
# append(): add something at the end of the list
letters.append("d")
# insert(): add object at a specific position in the list
letters.insert(0, "-")
# print(letters)

# remove
#
# pop(): remove the object at the end of the list
# It will remove only one item by index
letters.pop(0)
# remove(): remove an object by character
letters.remove("b")
# del: remove a range of items
del letters[0:3]
# clear: remove all the objects in the list
letters.clear()
print(letters)
