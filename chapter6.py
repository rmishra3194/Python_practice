import math

def area(radius):
    a = math.pi * radius**2
    return a

def absolute_value(x):
    if x < 0:
        return -x
    else:
        return x
    
def compare(x, y):
    if x > y:
        return 1
    elif x < y:
        return -1
    else:
        return 0




def distance(x1, y1, x2, y2):
    dx = x2 -x1
    dy = y2-y1
    dsquared = dx**2 + dy**2
    result = math.sqrt(dsquared)
    return result

def hypotenuse(a,b):
    c_squared = a**2 + b**2
    c = math.sqrt(c_squared)
    return c

def circle_area(xc, yc, xp, yp):
    return area(distance(xc, yc, xp, yp))

def is_divisible(x, y):
    if x % y == 0:
        return True
    else:
        return False

def is_divisible(x,y):
    return x % y == 0

def is_between(x, y, z):
    if x <= y <= z:
        return True
    else:
        return False

def factorial(n):
    if n == 0:
        return 1
    else:
        recurse = factorial(n-1)
        result = n * recurse
        return result



def fibonacci(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)

print(fibonacci(6))


def factorial(n):
    if not isinstance(n, int):
        print("Factorial is only defined for integers.")
        return None
    elif n < 0:
        print("Factorial is not defined for negative integers.")
        return None
    elif n == 0:
        return 1
    else:
        return n * factorial(n - 1)

#changes got saved in github