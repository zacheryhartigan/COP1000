"""
This program calculates prices for custom house signs.
"""



# Declare and initialize variables here.
# Charge for this sign.
charge = float(0.00)
# Number of characters
numChars = 8
numChars = float(input("How many Characters?"))
# Color of characters.
color = "gold"
color = input("What color?")
# Type of wood.
woodType = "oak"
woodType = input("What wood type?")

# Write assignment and if statements here as appropriate.
charge = float(35)
if numChars >5:
    charge = charge + ((numChars -5)*4)
if color == "gold":
    charge = charge + 15
if woodType == "oak":
    charge = charge + 20

# Output Charge for this sign.
print("The charge for this sign is $" + str(charge))
