# accessing items

letters = ["a", "b", "c", "d"]
letters[0] = "A"
print(letters[0:3])
print(letters[:3])
print(letters[0:])
print(letters[:])
print(letters)
print(letters[::2])


# OUTPUT
#
# ['A', 'b', 'c']
# ['A', 'b', 'c']
# ['A', 'b', 'c', 'd']
# ['A', 'b', 'c', 'd']
# ['A', 'b', 'c', 'd']
# ['A', 'c']

numbers = list(range(20))
print(numbers[::2])
print(numbers[::-1])

# OUTPUT
#
# [0, 2, 4, 6, 8, 10, 12, 14, 16, 18]
# [19, 18, 17, 16, 15, 14, 13, 12, 11, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0]
