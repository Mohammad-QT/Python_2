# Program Input
age = int(input("Enter age: "))
access_level = int(input("Enter access level (1-5): "))
security_code = int(input("Enter security code: "))
membership_input = input("Enter membership status (True/False): ")

# Convert membership input string to a boolean
membership_status = True if membership_input == "True" else False

# Input Validation
if age < 18 or access_level < 1 or access_level > 5 or security_code <= 0:
    print("Invalid input detected. Access denied.")
else:
    # Access Rules
    
    # Rule 3: Deny if Age < 21 AND Access Level < 5 (Evaluated first to ensure priority denial)
    if age < 21 and access_level < 5:
        print("Access Denied")
        
    # Rule 1: Access Level >= 4 AND Membership is True
    elif access_level >= 4 and membership_status == True:
        print("Access Granted")
        
    # Rule 2: Access Level >= 3 AND Security Code is even
    elif access_level >= 3 and security_code % 2 == 0:
        print("Access Granted")
        
    # Final Decision: Default deny if no grant rules are met
    else:
        print("Access Denied")