product1 = input("Enter the first product name: ")
price1 = float(input("Enter the price of " + product1 + ": "))

product2 = input("Enter the second product name: ")
price2 = float(input("Enter the price of " + product2 + ": "))

product3 = input("Enter the third product name: ")
price3 = float(input("Enter the price of " + product3 + ": "))

total = price1 + price2 + price3
average = total / 3

print("\nProduct        Price")
print("-----------------------")

print(format(product1, "12s"), format(price1, "7.2f"))
print(format(product2, "12s"), format(price2, "7.2f"))
print(format(product3, "12s"), format(price3, "7.2f"))

print("-----------------------")
print(format("Total: ", "12s"), format(total, "7.2f"))
print(format("Average: ", "12s"), format(average, "7.2f"))