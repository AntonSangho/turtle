from turtle import * 
import turtle
  

tur = turtle.Turtle()
  

tur.fillcolor("cyan")
  

tur.begin_fill()
  

for _ in range(4):
  tur.forward(200)
  tur.right(90)
  

tur.end_fill()
turtle.exitonclick()
