from math import sqrt
# Functions 

# 1 ------------- args -------------

def Sum(*args):
    print(sum(args), " ", type(args))

#Sum(1,2,3,5,6,5,4,3,35,5)

# 2 ------------ kwargs ------------

def Print(**kwargs):
    print(kwargs, " ", type(kwargs))

#Print(
    name = 'Mohammad',
    age = 20,
    bata = 'Bata!'
#)

# 3 ------------ lambda ------------

def Lamdba():
    
    f = lambda x: x+1
    square = lambda x: x*x
    cube = lambda x: x*x*x

    print(f(2), square(2), cube(2))

    applier = lambda F,x: F(x)
    print(applier(square, f(2)))

    applier2 = lambda G,F,x: G(F(x))
    print(applier2(cube ,square, f(2)))

    do = (lambda x: x*x) (100)
    #print(do(3)) TypeError: 'int' object is not callable
    print(do) 

# 4 ------------- map -------------

def Map():

    f = lambda x: x+1
    square = lambda x: x*x
    cube = lambda x: x*x*x

    List = [83 , 90 , 91 , 96 , 97 , 99]

    new_List = list(map(f,List))
    print("Grades Before: ", List)
    print("Grades After: ", new_List)

    print(list(map(float,List)))

    print("Cubes: ", list(map(cube,range(0,11))))

    seq=range (1,10)
    lam= lambda x,y: (x,y)
    print(list(map(lam , seq , map(square,seq))))

    def fun(x,y):
        return x * y, x + y

    num1= [1, 2, 3, 4, 5]
    num2= [10, 20, 30, 40, 50]

    L1 = list(map(lambda x,y : (x * y, x +y), num1, num2))
    print(L1)

    L2 = list(map(fun, num1, num2))
    print(L2)

    points = [(2, 1, 3), (5, 7, -3), (2, 4, 0), (9, 6, 8)]
    def distance(point) :
        x, y, z = point
        return sqrt(x**2 + y**2 + z**2)
    
    L = list(map(distance, points))

    print(L)

# 5 ------------- filter -------------
def Filter():

    nums = [0, 4, -7, 2, 1, 0 , -9 , 3, -5, 6, 8, 0, -3]
    
    obj = filter(lambda x : x != 0, nums)
    L = list(obj)

    print(L)

    positive = lambda x: x > 0
    pos = list(filter(positive,nums))

    print(pos)    

# 6 ------------- filter -------------

def Zip():

    a = ("John", "Charles", "Mike")
    #b = ("Jenny", "Christy", "Monica")
    b = ("Jenny", "Christy", "Monica", "Zain")

    x = zip(a, b)
    L = list(x)

    print(L)

Zip()