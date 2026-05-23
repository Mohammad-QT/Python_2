print("--- Q 1 ---")

def values(x):
    return x + 1, x * 2
a, b = values(5)
print(a, b)

print("\n--- Q 2 ---")

def makeSet():
    return {1, 2, 3, 2}
print(makeSet())

print("\n--- Q 3 ---")

s1 = {1, 2, 3}
s2 = {3, 4, 5}
print(s1 | s2)

print("\n--- Q 4 ---")

t = (2, 4, 6, 8)
print(t[1:3])

print("\n--- Q 5 ---")

s1 = {1, 2, 3}
s2 = {3, 4, 5}
print(s1 | s2)

print("\n--- Q 6 ---")

def mystery(x):
    return x, x**2, x**3
t = mystery(3)
print(t[1] + t[2])

print("\n--- Q 7 ---")

def operations(a, b):
    return {a + b, a * b, a - b}
print(operations(4, 2))

print("\n--- Q 8 ---")

s1 = {1, 2, 3, 4}
s2 = {3, 4, 5, 6}
print((s1 - s2) | (s2 - s1))

print("\n--- Q 9 ---")

def modify(t):
    L = list(t)
    L.append(10)
    return tuple(L)
x = (1, 2, 3)
print(modify(x))

print("\n--- Q 10 ---")

def calc(a, b):
    return {a, b}, (a + b, a * b)
x, y = calc(2, 3)
print(x)
print(y)

print("\n--- Q 11 ---")

def build(L):
    s = {x * 2 for x in L}
    return tuple(s)
print(build([1, 2, 2, 3]))