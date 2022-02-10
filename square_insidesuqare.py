from turtle import *
import turtle
tur=turtle.Turtle()
tur.speed(speed=1) #speed 1~10범위
for length in [45,40,30,30,25,20,15,10,5]:
    for x in range (4):

      tur.forward (length)

      tur.left (90)
