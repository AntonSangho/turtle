from turtle import *
import turtle

scrn = turtle.Screen()
tur = turtle.Turtle()

def drawSquares(tur, siz, num, angl):

    for i in range(num):
        for x in range(4):
            turtle.forward(siz)
            turtle.left(90)
        turtle.right(angl)

drawSquares(tur, 110, 5, 2)
