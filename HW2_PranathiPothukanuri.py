'''
Pranathi Pothukanuri
CS 100 2018F Section H05
HW 2 Sept 23, 2018
'''

import math

#1a
fac = math.factorial(100)
print(fac)

#1b
log1 = math.log2(1000000)
print(log1)

#1c
greatestcd = math.gcd(63, 49)
print(greatestcd)

#2
import turtle
pen = turtle.Turtle()
paper = turtle.Screen()
paper.bgcolor("lightblue")
pen.width(10)

pen.penup();

pen.goto(0, -300)

def square(p, sideLength):
    p.pd()
    for i in range(4):
        p.forward(sideLength)
        p.left(90)

pen.color("blue")
square(pen, 100)

pen.pu()
pen.goto(40, -250)
pen.pd()
pen.write("HOUSE")
pen.pu()
pen.goto(0, -300)
pen.pd()
pen.left(90)

pen.forward(100)

pen.right(30)

def triangle(pe,sLength):
    pe.pd()
    for i in range(3):
        pen.forward(sLength)
        pen.right(120)

pen.color("red")

triangle(pen,100)


pen.pu()
pen.right(150)

pen.forward(100)

pen.right(90)

pen.forward(50)

def pentagonRight (penn, siLength):
    pen.pd()
    for i in range(5):
        pen.forward(siLength)
        pen.right(72)
        
def pentagonLeft (pen1, sidLength):
    pen.pd()
    for i in range(5):
        pen.forward(sidLength)
        pen.left(72)

pen.color("green")
pentagonRight(pen, 100)
pen.pu()
pen.forward(175)
pentagonRight(pen, 100)
pen.left(180)
pen.pu()
pen.forward(375)
pentagonLeft(pen, 100)

#3
pen.width(20)
radius = 50
pen.color("yellow")
for i in range(4):
    pen.pu()
    pen.goto(-100,(50-radius) + 60)
    pen.pd()
    pen.circle(radius)
    radius = radius + 50

pen.pu()
pen.goto(200, 60)
pen.pd()
pen.write("<== SUN")

    
    
    




    
    

