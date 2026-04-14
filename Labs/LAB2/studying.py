print ("Task One")

print (3 < 5)  # True
print (3 < 5 and 5 < 3)  # False
print (3 < 5 or 5 < 3)  # True
print (True and False)  # False
print (True or False)   # True
print (not True)        # False
print (not False and True)  # True
print (True and False and True)  # False
print (True or (False and True))  # True
# print ((5/0==1) and False)  # False (this will raise a ZeroDivisionError)
print (False and (5/0==1))  # False (this will raise a ZeroDivisionError)
print (bool(1 and 2))   # True
print (bool(5 and 0))   # False

print ("Task Two")

print (float(4))  
print (int(5.3))  
print (int(True))  
print (float(int(5.3)))  
print (float(7) // 4)  
print (int(7 / 4))  
print (6.2 and False)  
print (True and 6.2)  
print (type(4.5))  
print (type(True and 3)) # how is it not boolean , it says int because the and operator returns the last evaluated operand, which in this case is 3. Since 3 is an integer, the type of the expression True and 3 is int.
print (type(3 and True))