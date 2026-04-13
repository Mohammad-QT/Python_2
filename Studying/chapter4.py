from math import pi

def Circle_Area():
    
    radius = float(input(print("Enter radius: ")))

    if radius >= 0:
        area = pi * radius**2
        print (f"The Circle of Radius {radius} is {area} Area !")
    else: 
        print ("Radius cant be Minus")

def leapYear ():
    year = int(input(print("Enter a Year: ")))

    if year % 400 == 0:
        leapYear=True
    elif year % 100 == 0:
        leapYear=False
    elif year % 4 == 0:
        leapYear=True
    else:
        leapYear=False
    
    if leapYear == True:
        print(f"Year {year} is a Leap Year")
    else: 
        print(f"Year {year} is not a Leap Year")

def LEAPYEAR ():
    year = int(input(print("Enter a Year: ")))

    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                LEAPYEAR=True
        else: LEAPYEAR=True
    else: LEAPYEAR=False

    if LEAPYEAR == True:
        print(f"Year {year} is a Leap Year")
    else: 
        print(f"Year {year} is not a Leap Year")

def Leap_Year():
    year = int(input(print("Enter a Year: ")))  
    
    if (year % 4 == 0 and not(year % 100 == 0) or year % 400 == 0):
        Leap_Year = True
    else: Leap_Year = False

    if Leap_Year == True:
        print(f"Year {year} is a Leap Year")
    else: 
        print(f"Year {year} is not a Leap Year")

def Parity():
    n = int(input(print("Enter a Number: ")))  
    parity = "Even" if n % 2 == 0 else "Odd"
    print(f"Number is {parity}")


def Max():
    x = int(input(print("Enter X: ")))
    y = int(input(print("Enter Y: ")))    

    max = x if x > y else y
    print(f"Max number is {max}")

Max()