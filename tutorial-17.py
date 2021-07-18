# nested loops

# outer loop
for x in range(5):
    # inter loop - child of outer loop
    for y in range(3):
        print(f"({x},  {y})")

# OUTPUT:
#
# (0,  0)
# (0,  1)
# (0,  2)
# (1,  0)
# (1,  1)
# (1,  2)
# (2,  0)
# (2,  1)
# (2,  2)
# (3,  0)
# (3,  1)
# (3,  2)
# (4,  0)
# (4,  1)
# (4,  2)
