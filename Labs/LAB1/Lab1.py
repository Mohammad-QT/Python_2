import math
import random

# --- Part 1: Arithmetic Expressions ---
print("--- Part 1: Arithmetic Expressions ---")
print("2 * 3 =", 2 * 3)
print("2 ** 3 =", 2 ** 3)
print("5 + 2 * 5 =", 5 + 2 * 5)
print("(5 + 2) * 5 =", (5 + 2) * 5)
print("-4 - -4 - -4 =", -4 - -4 - -4)
print("2 ** 2 ** 0 =", 2 ** 2 ** 0)
print("(2 ** 2) ** 0 =", (2 ** 2) ** 0)
print("6 // 2 =", 6 // 2)
print("6 // 4 =", 6 // 4)
print("6.0 / 4.0 =", 6.0 / 4.0)
print("2.0 // 2.5 =", 2.0 // 2.5)
print("9.0 * 0.5 =", 9.0 * 0.5)
print("9.0 ** 0.5 =", 9.0 ** 0.5)
print("6 % 2 =", 6 % 2)
print("8 % 3 =", 8 % 3)
print("6.2 % 4 =", 6.2 % 4)

# --- Part 2: Type Conversion and Built-in Functions ---
print("\n--- Part 2: Type Conversion ---")
print("float(4):", float(4))
print("int(5.3):", int(5.3))
print("float(int(5.3)):", float(int(5.3)))
print("int(5.7):", int(5.7))
print("float(7) // 4:", float(7) // 4)
print("int(7 / 4):", int(7 / 4))
print("type(4.5):", type(4.5))
print("type(7):", type(7))
print("str(25):", str(25))

# --- Part 3: Using the math Module ---
print("\n--- Part 3: Math Module ---")
print("math.floor(7.8):", math.floor(7.8))
print("math.ceil(7.2):", math.ceil(7.2))
print("round(6.58):", round(6.58))
print("round(6.583, 2):", round(6.583, 2))
print("abs(-15):", abs(-15))
print("pow(2, 4):", pow(2, 4))
print("math.sqrt(81):", math.sqrt(81))

# --- Part 4: Random Number Generation ---
print("\n--- Part 4: Random Numbers ---")
print("randint(1, 10):", random.randint(1, 10))
print("randint(50, 100):", random.randint(50, 100))
print("random():", random.random())
print("randrange(0, 20, 2):", random.randrange(0, 20, 2))

# --- Part 5: Using the print() Function ---
print("\n--- Part 5: Print Function Demo ---")
print("This is normal printing.")
print("Printing", "multiple", "values", 100)
print("Apple", "Orange", "Banana", sep=" | ")
print("This stays on the ", end="")
print("same line.")
print("I am", 20, "years old.")

# --- Part 6: Formatted Output ---
print("\n--- Part 6: Student Information ---")
name = "Mohammad Ismael Salman AlQatamesen"
student_id = "32023**********"
major = "Computer Science/AI"

print(format("Name:", "12s"), format(name, "s"))
print(format("ID:", "12s"), format(student_id, "s"))
print(format("Major:", "12s"), format(major, "s"))