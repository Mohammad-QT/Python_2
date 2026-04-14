age = int(input("Enter age: "))
access_level = int(input("Enter access level (1-5): "))
security_code = int(input("Enter security code: "))
membership_input = input("Enter membership status (True/False): ")

if age < 18 or access_level < 1 or access_level > 5 or security_code < 0:
    print("Invalid input. Please enter valid age, access level, and security code.")
else:
    membership = membership_input.lower() == 'true'
    
    if ( access_level >= 4 and membership) or (access_level >= 3 and security_code % 2 == 0):
        print("Access Granted")
    elif age < 21 and access_level < 5:
        print("Access Denied")
    else:
        print("Access Denied")