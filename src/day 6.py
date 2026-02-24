def mul(a,b):
    print(a*b)
    
result=mul(2,4)
print(result)

#global & Local ver 1

X=13

def show_varaible():
    X=20
    print(X)
    
show_varaible()
print(X)

#2

count=0

def increase():
    global count
    count+=1
    
increase()
print(count)
    
#3

import math
import random

print(math.sqrt(6)) 
print(random.randint(2,6))

#
from math import sqrt

print(math.sqrt(9))


#task1
def calc_rectangle(length, width):
    area = length * width
    perimeter = 2 * (length + width)
    return area, perimeter 

# Input of length and width
length = int(input("Enter the length: "))
width = int(input("Enter the width: "))

# Assigning the variables
area, perimeter = calc_rectangle(length, width)

# Printing the values
print(f"The area of rectangle is {area}")
print(f"The perimeter of rectangle is {perimeter}")