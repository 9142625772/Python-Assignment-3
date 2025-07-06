#Module 4: Functions & Modules in Python

#Task 1:

def factorial(n):
             if n<2:
                     return 1
             else:
                     return n* factorial(n-1)

num=int(input("Enter a number:"))
result=factorial(num)
print("Factoial of",num,"is:",result)

#Task 2: Using the Math Module for Calculations

import math
#1. Asks the user for a number as input.
num=int(input("Enter a number:"))

#2. Uses the math module to calculate the:
#Square root of the number
# Natural logarithm (log base e) of the number
#oSine of the number (in radians)

sqrt=math.sqrt(num)

log=math.log(num)

sin=math.sin(num)

#3. Displays the calculated results.
print("Squar root:",sqrt)
print("logarithm:",log)
print("sine",sin)


