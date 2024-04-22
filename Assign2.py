"""
Write a program that does the following:
Asks the user to enter in 2 numbers that can be float values
Ask the user if one of the numbers is the hypotenuse of a right triangle
Calculates the length of the missing side and rounds it to 1 decimal place.
"""

x = float(input("Enter a number: "))
y = float(input("Enter another number: "))
z = str((input("Is there a number that's the hypotenues? (Answer yes or no):  ")))
if z == "yes":
    L = (max(x,y)**2 - min(x, y)**2)**0.5
    round(L, 1)
    print(f"the missing length is {L}")
else:
    L = (x**2 + y**2)**0.5
    round(L, 1)
    print(f"the missing length is {L}")
