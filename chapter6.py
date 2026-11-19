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

#6.1

def b(z):
    prod = a(z, z)
    print(z, prod)
    return prod

def a(x, y):
    x = x + 1
    return x * y

def c(x , y, z):
    total = x + y + z
    square = b(total)**2
    return square


#6.2 

def ack(m,n):
    if m == 0:
        return n + 1
    elif m > 0 and n == 0:
        return ack(m -1, 1)
    elif m > 0 and n > 0:
        return ack(m -1, ack(m, n -1))

print(ack(1 , 1))

#6.3

def first(word):
    return word[0]

def last(word):
    return word[-1]

def middle(word):
    return word[1: -1]


def is_palindrome(word):
    if len(word) <= 1:
        print("The word is a palindrome.")
    elif first(word) != last(word):
        print("The word is not a palindrome.")
    else:
        is_palindrome(middle(word))
  
word = input("Enter a word: ")
is_palindrome(word)

def is_palindrome():
    word = input("Enter a word: ")

    if word == word[::-1]:
        print("The word is a palindrome.")
    else:
        print("The word is not a palindrome.")

def is_palindrome(text):
    if len(text) <= 1:
        return True
    elif text[0] != text[-1]:
        return False
    else:
        return is_palindrome(text[1:-1])

text = input("Enter a word: ")
is_palindrome(text)













#6.4
def is_power(a, b):
    if a == 1:
        return True
    elif b == 0:
        return False
    elif a % b != 0:
        return False    
    else:   
        return is_power(a // b, b)




def is_power(a, b):
    if a == 1:
        return True
    elif b == 0:
        return a == 0
    elif a == 0 or b == 1:
        return False
    elif a % b != 0:
        return False
    else:
        return is_power(a // b, b)



#6.5
def gcd(a,b):
    if b == 0:
        return a

    return gcd(b , a%b) 

