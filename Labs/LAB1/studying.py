import math
from random import *

print("Part 1 – Arithmetic Expressions")

print (2 * 3) # 6
print (2 ** 3) # 8
print (5 + 2 * 5) # 15
print ((5 + 2) * 5) # 35
print (-4 - -4 - -4) # 4
print (2 ** 2 ** 0) # 2
print ((2 ** 2) ** 0) # 1
print (6 // 2) # 3
print (6 // 4) # 1
print (6.0 / 4.0) # 1.5
print (2.0 // 2.5) # 0.0 floor division operator (//) returns the largest integer less than or equal to the result of the division. In this case, 2.0 divided by 2.5 is 0.8, and the largest integer less than or equal to 0.8 is 0. Therefore, the result of 2.0 // 2.5 is 0.0.
print (2.0 / 2.5) # 0.8
print (9.0 * 0.5) # 4.5
print (9.0 ** 0.5) # 3.0
print (6 % 2) # 0
print (8 % 3) # 2
print (6.2 % 4) # 2.2

print ("Part 2 - Type Conversion and Built-in Functions")

print (float(4)) 
print (int(5.3)) 
print (float(int(5.3))) 
print (int(5.7)) 
print (float(7) // 4) 
print (int(7 / 4)) 
print (type(4.5)) 
print (type(7)) 
print (str(25))

print ("Part 3 – Using the math Module")

print (math.floor(7.8)) #7
print (math.ceil(7.2)) #8
print (round(6.58)) #7
print (round(6.2)) #6
print (round(6.583,2)) #6.58
print (abs(-15)) #15
print (pow(2,4)) #16
print (math.sqrt(81)) #9

print ("Part 4 – Random Number Generation")

print (randint(1,10)) # 1-10 (both are included)
print (randint(50,100)) # 50-100 (both are included)
print (random()) # 0.0 - 1.0 (both are included)
print (randrange(0,20,2)) # 0, 2, 4, 6, 8, 10, 12, 14, 16, 18 (Here not both are included, and the step is 2)

print ("Part 5 – Using the print() Function")

name = "Mohammad"
age = 20

print ("Hello, World")
print ("Hello", "World", sep="-") # Hello-World
print ("Hello", "World", end="!") # Hello World!
print (f"My name is {name} and I am {age} years old.") # My name is Mohammad and I am 20 years old.

print ("Part 6 – Formatted Output")

# Create a formatted section displaying student information such as name, student ID, and major. 
student_name = "Mohammad"
student_id = "S12345"
student_major = "Computer Science"

print(format("Name:", "12s"), format(student_name, "s"))
print(format("ID:", "12s"), format(student_id, "s"))
print(format("Major:", "12s"), format(student_major, "s"))
# and what is the difference between fs and s and else are there any other options for formatting?
# The 's' format specifier is used for strings, while 'f' is used for floating-point numbers. The 's' specifier will simply display the string as it is, while 'f' will format the number to a specific number of decimal places. For example, if you use '{:.2f}'.format(3.14159), it will display '3.14'. There are also other format specifiers such as 'd' for integers, 'e' for scientific notation, and 'x' for hexadecimal representation.
