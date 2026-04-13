from math import *

print(sin.__doc__)

upper = 'A'
diff = ord('a') - ord('A')  # 32
print(chr(ord(upper) + diff), end='')

print("Look at this")

print(1, 1, 2026, sep='/')

print("Name and Price of every Product," \
" If you want to quit, enter 'q' as the name of the product")

products = []
total = 0
avg = 1

while True:
    name = input("Enter the name of the product: ").lower()
    if name == 'q':
        break
    try:
        price = float(input("Enter the price of the product: "))
        total += price
    except ValueError:
        print("Invalid price. Please enter a number.")
        continue
    products.append((name, price))

avg = total / len(products) if products else 0

print("\nProduct                   Price")
print("\n---------------------------------")
for name, price in products:
    print(format(name, '20s'), format(price, '10.2f'))
print("---------------------------------")
print(format("\nTotal", '20s'), format(total, '10.2f'))
print(format("Average", '20s'), format(avg, '10.2f'))
print("number of products:", len(products))
