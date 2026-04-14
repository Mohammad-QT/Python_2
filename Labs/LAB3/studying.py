glasses = input("Which glasses do you want to buy? non-prescription/prescription (1/2): ").lower()
total = 0

while glasses != "1" and glasses != "2":
    print("Invalid input. Please enter 1 for non-prescription or 2 for prescription.")
    glasses = input("Which glasses do you want to buy? non-prescription/prescription (1/2): ").lower()

if (glasses == "2"):
    total += 40.00
    addition = input("Do you want to add a tint glass or anti-glare ? (1/2): ").lower()

    while addition != "1" and addition != "2":
        print("Invalid input. Please enter 1 for tint glass or 2 for anti-glare.")
        addition = input("Do you want to add a tint glass or anti-glare ? (1/2): ").lower()

    if(addition == "1"):
        total += 12.50

    elif(addition == "2"):
        total += 9.99

elif (glasses == "1"):
    total += 25.00

print(f"Your total cost is ${total}")