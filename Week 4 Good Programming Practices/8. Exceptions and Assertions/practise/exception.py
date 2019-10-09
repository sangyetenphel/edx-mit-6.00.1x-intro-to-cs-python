# -*- coding: utf-8 -*-
"""
Created on Fri Sep 27 22:17:42 2019

@author: Sangye Tenphel
"""

# =============================================================================
# try:
#     a = int(input("Tell me one number:"))
#     b = int(input("Tell me another number:"))
#     print(a/b) 
#     print ("Okay") 
# except: 
#     print("Bug in user input.")
# print("Outside")
# =============================================================================

# =============================================================================
# try:                                        # this is the code that you will try to run. What happens after this depends on whether an exception was thrown or not.
#     print("Could not convert to a number.")
#     a = int(input("Tell me one number: "))
#     b = int(input("Tell me another number: "))
#     print("a/b = ", a/b)
#     print("a+b = ", a+b)
# 
# except ValueError:                          # only execute if these errors come up
#     print("Could not convert to a number.")        
# except ZeroDivisionError:                   # only execute if these errors come up
#     print("Can't divide by zero")
# except:                                     # this block handles the exception if it occurs when the try block is executed.    
#     print("Something went very wrong.")     
# else:                                       # this code block runs only if no exceptions were thrown in the try block.
#     print('I reached here cause no execeptions were raised.') 
# finally:                                    # this block always runs, even if there were exceptions in the try block. As noted in the lecture, this block if very helpful for “clean up code” such as closing files.
#     print('I am very stubborn!')
# =============================================================================
    
# =============================================================================
# def a(x, y):
# try:
#     print("Initial code...")
#     print(x[y])
#     print(x/y)
# except Exception as e:                        # handling all exceptions
#     print(e)
# =============================================================================
def printElement(lst, index):
    try:
        print(lst[index])
    except IndexError as e:                     # handling specific error exceptions
        print(e)
    