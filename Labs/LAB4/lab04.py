
def double(y):
    x = 2
    return x * y
res = double(5)
print(res)

x = 10
def test1():
    x = 5
    print(x)
test1()
print(x)

x = 10
def test2():
    global x
    x = 5
test2()
print(x)

# 2. Function square(x)

def square(x):
    return x ** 2


# 3. Function sumToN(n)

def sumToN(n):
    total = 0
    
    for i in range(1, n + 1):
        total += i
    return total


# 4. Program including cube(x) and avg(a, b, c)

def cube(x):
    """Returns x cubed"""
    return x ** 3

def avg(a, b, c):
    """Returns the average of three numbers"""
    return (a + b + c) / 3

print(f"Square of 4: {square(4)}")
print(f"Sum from 1 to 5: {sumToN(5)}")
print(f"Cube of 3: {cube(3)}")
print(f"Average of 10, 20, 30: {avg(10, 20, 30)}")