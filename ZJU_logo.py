# coding:utf-8
"""
using python to draw Zhejiang University's logo
"""
import turtle

def drawLeftHead(pos, ratio):
    # move the pen
    turtle.penup()
    turtle.goto(pos)
    turtle.pendown()
    # draw
    turtle.right(40)
    turtle.forward(10 * ratio)
    turtle.right(10)
    turtle.forward(60 * ratio)
    turtle.left(125)
    turtle.forward(60 * ratio)
    return turtle.pos()

def drawRightHead(pos, ratio):
    # move the pen
    turtle.penup()
    turtle.goto(pos)
    turtle.pendown()
    # draw
    turtle.forward(20 * ratio)
    turtle.right(5)
    turtle.forward(10 * ratio)
    turtle.right(5)
    turtle.forward(30 * ratio)
    turtle.right(150)
    turtle.forward(40 * ratio)
    turtle.left(90)
    turtle.forward(50 * ratio)
    turtle.left(120)
    turtle.forward(60 * ratio)
    turtle.right(10)
    turtle.forward(10 * ratio)
    turtle.right(40)
    return turtle.pos()

def drawLeftWing(pos, ratio):
    # move the pen
    turtle.penup()
    turtle.goto(pos)
    turtle.pendown()
    # draw
    turtle.right(110)
    for i in range(10):
        turtle.left(15)
        turtle.forward(4 * ratio)

    turtle.right(10)
    turtle.forward(10 * ratio)
    turtle.right(20)
    turtle.forward(5 * ratio)
    turtle.right(20)
    turtle.forward(25 * ratio)
    turtle.right(125)
    turtle.forward(40 * ratio)

    turtle.left(120)
    turtle.forward(25 * ratio)
    turtle.left(60)
    turtle.forward(10 * ratio)
    turtle.left(10)
    turtle.forward(10 * ratio)
    turtle.right(30)
    turtle.forward(10 * ratio)
    turtle.right(20)
    turtle.forward(30 * ratio)
    turtle.right(140)
    turtle.forward(50 * ratio)

    turtle.left(120)
    turtle.forward(25 * ratio)
    turtle.left(60)
    turtle.forward(10 * ratio)
    turtle.left(10)
    turtle.forward(10 * ratio)
    turtle.right(20)
    turtle.forward(10 * ratio)
    turtle.right(20)
    turtle.forward(40 * ratio)
    turtle.right(150)
    turtle.forward(60 * ratio)

    turtle.left(120)
    turtle.forward(25 * ratio)
    turtle.left(60)
    turtle.forward(30 * ratio)
    turtle.left(10)
    turtle.forward(10 * ratio)
    turtle.right(20)
    turtle.forward(10 * ratio)
    turtle.right(20)
    turtle.forward(45 * ratio)
    turtle.right(150)
    turtle.forward(80 * ratio)

    turtle.left(120)
    turtle.forward(25 * ratio)
    turtle.left(60)
    turtle.forward(30 * ratio)
    turtle.left(10)
    turtle.forward(10 * ratio)
    turtle.right(20)
    turtle.forward(10 * ratio)
    turtle.right(20)
    turtle.forward(50 * ratio)
    turtle.right(150)
    turtle.forward(150 * ratio)

    return turtle.pos()

def drawRightWing(pos, ratio):
    # move the pen
    turtle.penup()
    turtle.goto(pos)
    turtle.pendown()
    # draw
    turtle.forward(150 * ratio)
    turtle.right(150)
    turtle.forward(50 * ratio)
    turtle.right(20)
    turtle.forward(10 * ratio)
    turtle.right(20)
    turtle.forward(10 * ratio)
    turtle.left(10)
    turtle.forward(30 * ratio)
    turtle.left(60)
    turtle.forward(25 * ratio)
    turtle.left(120)

    turtle.forward(80 * ratio)
    turtle.right(150)
    turtle.forward(50 * ratio)
    turtle.right(20)
    turtle.forward(10 * ratio)
    turtle.right(20)
    turtle.forward(10 * ratio)
    turtle.left(10)
    turtle.forward(30 * ratio)
    turtle.left(60)
    turtle.forward(25 * ratio)
    turtle.left(120)

    turtle.forward(60 * ratio)
    turtle.right(150)
    turtle.forward(40 * ratio)
    turtle.right(20)
    turtle.forward(10 * ratio)
    turtle.right(20)
    turtle.forward(10 * ratio)
    turtle.left(10)
    turtle.forward(10 * ratio)
    turtle.left(60)
    turtle.forward(25 * ratio)
    turtle.left(120)

    turtle.forward(50 * ratio)
    turtle.right(140)
    turtle.forward(30 * ratio)
    turtle.right(20)
    turtle.forward(10 * ratio)
    turtle.right(30)
    turtle.forward(10 * ratio)
    turtle.left(10)
    turtle.forward(10 * ratio)
    turtle.left(60)
    turtle.forward(25 * ratio)
    turtle.left(120)

    turtle.forward(40 * ratio)
    turtle.right(140)
    turtle.forward(30 * ratio)
    turtle.right(20)
    turtle.forward(10 * ratio)
    turtle.right(30)
    turtle.forward(10 * ratio)
    turtle.left(10)
    for i in range(10):
        turtle.left(15)
        turtle.forward(4 * ratio)

    return turtle.pos()

def drawTail(pos, ratio):
    # move the pen
    turtle.penup()
    turtle.goto(pos)
    turtle.pendown()
    # draw
    turtle.right(105)
    turtle.forward(90 * ratio)
    turtle.right(90)
    turtle.forward(90 * ratio)
    return turtle.pos()

def drawEagle(pos=(0, 100), ratio=1, rotation=0):
    turtle.penup()
    turtle.goto(pos)
    turtle.pendown()
    turtle.right(rotation)

    turtle.begin_fill()

    # draw the head's right part
    newPos = drawRightHead(pos, ratio)

    # draw the right wing
    newPos = drawRightWing(newPos, ratio)

    # draw the tail
    newPos = drawTail(newPos, ratio)

    # draw the left wing
    newPos = drawLeftWing(newPos, ratio)

    # draw the head's left part
    drawLeftHead(newPos, ratio)

    turtle.goto(pos)
    turtle.end_fill()


if __name__ == "__main__":
    # Initialize
    turtle.pensize(4)
    turtle.speed(8)
    turtle.pencolor('blue')
    turtle.fillcolor('pink')
    turtle.hideturtle()
    # draw the logo
    drawEagle()
    turtle.done()
