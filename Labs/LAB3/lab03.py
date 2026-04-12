total_cost = 0.0

print("What kind of glasses would you like:")
glasses_choice = int(input("1 -> prescription, 2 -> non-prescription: "))

while glasses_choice != 1 and glasses_choice != 2:
    glasses_choice = int(input("1 -> prescription, 2 -> non-prescription: "))

if glasses_choice == 1:
    total_cost += 40.00
    
    print("What kind of coating would you like:")
    coating_choice = int(input("1 -> anti-glare, 2 -> brown tint: "))
    
    while coating_choice != 1 and coating_choice != 2:
        coating_choice = int(input("1 -> anti-glare, 2 -> brown tint: "))
        
    if coating_choice == 1:
        total_cost += 12.50
    elif coating_choice == 2:
        total_cost += 9.99
        
elif glasses_choice == 2:
    total_cost += 25.00

print(f"Your total cost is ${total_cost}")