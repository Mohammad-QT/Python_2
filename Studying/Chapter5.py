#text = input("Write smth to change it to oppisite case: ")

#text = text.swapcase()

def opposite_case(text):
    
    for i in text:
        if i == i.lower():
            print(i.upper(), end="")
        else:
            print(i.lower(), end="")

s = "Hello123"
s1 = "   "
s2 = "Hello World"
s3 = "HelloWorld"
s4 = "12345"
s5 = "Hello123"
s6 = "HELLO"

print("s.isalnum():\n","s", s.isalnum(), "s1", s1.isalnum(), "s2", s2.isalnum(), "s3", s3.isalnum(), "s4", s4.isalnum(), "s5", s5.isalnum(), "s6", s6.isalnum()) #True , because it contains only letters and numbers
print("s.isalpha():\n", "s", s.isalpha(), "s1", s1.isalpha(), "s2", s2.isalpha(), "s3", s3.isalpha(), "s4", s4.isalpha(), "s5", s5.isalpha(), "s6", s6.isalpha()) #False , because it contains numbers
print("s.isdigit():\n", "s", s.isdigit(), "s1", s1.isdigit(), "s2", s2.isdigit(), "s3", s3.isdigit(), "s4", s4.isdigit(), "s5", s5.isdigit(), "s6", s6.isdigit()) #False , because it contains letters
print("s.isidentifier():\n", "s", s.isidentifier(), "s1", s1.isidentifier(), "s2", s2.isidentifier(), "s3", s3.isidentifier(), "s4", s4.isidentifier(), "s5", s5.isidentifier(), "s6", s6.isidentifier()) # True , because it can be used as a variable name (it starts with a letter and contains only letters and numbers)
print("s.islower():\n", "s", s.islower(), "s1", s1.islower(), "s2", s2.islower(), "s3", s3.islower(), "s4", s4.islower(), "s5", s5.islower(), "s6", s6.islower()) #False , because it contains uppercase letters
print("s.isupper():\n", "s", s.isupper(), "s1", s1.isupper(), "s2", s2.isupper(), "s3", s3.isupper(), "s4", s4.isupper(), "s5", s5.isupper(), "s6", s6.isupper()) #False , because it contains lowercase letters
print("s.isspace():\n", "s", s.isspace(), "s1", s1.isspace(), "s2", s2.isspace(), "s3", s3.isspace(), "s4", s4.isspace(), "s5", s5.isspace(), "s6", s6.isspace()) #False , because it contains non-whitespace characters

