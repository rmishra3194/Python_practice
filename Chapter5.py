import time
import turtle
bob = turtle.Turtle()

def current_time():
    now =  time.localtime()
    hours = now.tm_hour
    minutes = now.tm_min
    seconds = now.tm_sec
    days = int(time.time() // (24 * 60 * 60))
    print(f"Current time: {hours:02d}:{minutes:02d}:{seconds:02d}")
    print(f"Days since epoch: {days}")

def check_fermat(a, b, c, n):
    if n > 2 and a**n + b**n == c**n:
        print("Holy smokes, Fermat was wrong!")
    else:
        print("No, that doesn't work.")
        



def check_fermat_input():
    a = int(input("Enter a: "))
    b = int(input("Enter b: "))
    c = int(input("Enter c: "))
    n = int(input("Enter n: "))
    check_fermat(a, b, c, n)

def is_triangle(a, b, c):
    if a + b > c and b + c > a and c + a > b:
        print("Yes")
    else:
        print("No")

def is_triangle_input():
    a = int(input("Enter a: "))
    b = int(input("Enter b: "))
    c = int(input("Enter c: "))
    is_triangle(a, b, c)

def recurse(n, s):
    if n == 0:
        print(s)
    else:
        recurse(n-1, s+n)

def n_factorial(n):
    if n == 0:
        return 1
    else:
        return n * n_factorial(n-1)

def draw(t, length, n):
    if n == 0:
        return
    angle = 50
    t.fd(length*n)
    t.lt(angle)
    draw(t, length, n-1)
    t.rt(2*angle)
    draw(t, length, n-1)
    t.lt(angle)
    t.bk(length*n)



def koch(t, length):
    if length < 3:
        t.fd(length)
        return
    
    koch(t, length/3)
    t.lt(60)
    koch(t, length/3)
    t.rt(120)
    koch(t, length/3)
    t.lt(60)
    koch(t, length/3)


def snowflake(t, length, n):
    for i in range(n):
        koch(t, length)
        t.rt(360/n)



koch(bob, 100)