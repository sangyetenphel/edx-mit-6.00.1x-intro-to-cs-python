# -*- coding: utf-8 -*-
"""
Created on Fri Sep  6 18:22:03 2019

@author: Sangye Tenphel
"""

#guess = 0
x = int(input("Enter an integer: "))

# =============================================================================
# while guess**3 < abs(x): # abs to convert to positive to solve for negative values
#     guess += 1
#     
# if guess**3 == abs(x):
#     if x < 0: # check if original value was -ve, if so add the -ve sign infront of the guess(cube root)
#         guess = -guess
#     print("The cube root of", x, "is:", guess)
# else:
#     print("The cube root doesn't exist.")
# =============================================================================


# Same idea but using a for loop 
for i in range(abs(x) + 1):
    if i**3 >= abs(x):
        break
    
if i**3 != abs(x):
    print(i, "is not a perfect cube")
else:
    if x < 0:
        i = -i
    print("The cube root of " + str(x) + " is " + str(i))

