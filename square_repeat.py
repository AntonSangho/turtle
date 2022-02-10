from turtle import *
import turtle

turtle.right(180)

turtle.speed(0)

leng = 500

for times in range (100):
  for endtimes in range (4):
    turtle.forward(leng)
    turtle.right(90)
  leng -= 6
