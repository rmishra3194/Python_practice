import turtle
import math

bob = turtle.Turtle()
print(bob)

def polyline(t, n, angle, length):
  for i in range(n):
    t.fd(length)
    t.lt(angle)

def polygon(t, n, length):
	angle = 360.0 / n 
	polyline(t, n, angle, length)

def arc(t, r, angle):
	circumference = 2 * math.pi * r
	arc_length = circumference * angle / 360
	n = int(arc_length / 3) + 1 
	step_length = arc_length / n
	step_angle = float(angle) / n
	polyline(t, n, step_angle, step_length)

def circle(t,r):
	arc(t, r, 360)

def square(t, length):
    for i in range(4):
        t.fd(length)
        t.lt(90)

def polygon(t, n, length):
    angle = 360 / n
    for i in range(n):
        t.fd(length)
        t.lt(angle)

def circle(t, r):
    circumference = 2 * math.pi * r
    n = int(circumference / 3) + 1
    length = circumference / n 
    polygon(t, n, length)


def pie(t, n, radius):
     angle = 360 /n
     side = 2 * radius * math.sin(math.radians(angle/2))
     corner_angle = 90 + angle / 2

     for i in range(n):
          t.fd(radius)
          t.lt(corner_angle)
          t.fd(side)
          t.lt(corner_angle)
          t.fd(radius)
          t.lt(180)

#pie(bob, 7, 100)

def basic_flower(t, r, n): #The size of the petals get smaller with more petals
    starting_angle = 360/n #Angle of the petal's beginning
    returning_angle = 180 - starting_angle #Angle at the petal tip to return to starting position
   
    for i in range(n):
        #Petals
        arc(t, r, starting_angle)
        t.lt(returning_angle)
        arc(t, r, starting_angle)
 
        #Set up cursor for next petal
        t.lt(returning_angle)
        t.lt(starting_angle)
 
#basic_flower(turtle, 100, 7)
#basic_flower(turtle, 300, 20)
 
#basic_flower(turtle, 100, 10)
#basic_flower(turtle, 200, 10)
 
 
 
def angled_flower(t, r, n, angle): #The size of the petals get smaller with more petals
    returning_angle = 180 - angle #Angle at the petal tip to return to starting position
   
    for i in range(n):
        #Petals
        arc(t, r, angle)
        t.lt(returning_angle)
        arc(t, r, angle)
 
        #Set up cursor for next petal
        t.lt(returning_angle)
        t.lt(angle)
 
    t.lt(returning_angle)
 
def angled_flower_overlapped(t, r, n, angle):
    angled_flower(t, r, n, angle)
    angled_flower(t, r, n, angle)
 
 
#angled_flower_overlapped(turtle, 100, 5, 72) #360/5 = angle

def petals(t, r, angle):
     for i in range(2):
          arc(t, r, angle)
          t.lt(180 - angle)

def flower(t, r, n, angle):
     for i in range(n):
          petals(t, r, angle)
          t.lt(360 / n)

#bob.speed(40)
#petals(bob, 100, 60)
#flower(bob, 100, 10, 70)

def z(t):
     t.fd(100)
     t.lt(45)
     t.bk(100 * math.sqrt(2))
     t.rt(45)
     t.fd(100)

def A(t, length):
     t.lt(60)
     t.fd(length)
     t.rt(120)
     t.fd(length)
     t.bk(length/2)
     t.rt(120)
     t.fd(length/2)

def B(t, length):
     t.lt(90)
     t.bk(length)
     t.rt(90)
     t.circle(length/4, 180)
     t.rt(180)
     t.circle(length/4, 180)
     
     

#B(bob, 100)
def spiral(t):
    a = 0
    b = 3
    max_angle = 5 * 2 * math.pi  # 5 full turns
    step = 0.05  # Smaller step = smoother curve

    theta = 0
    while theta <= max_angle:
     r = a + b * theta
     x = r * math.cos(theta)
     y = r * math.sin(theta)
     t.goto(x, y)
     theta += step

spiral(bob)
turtle.mainloop()