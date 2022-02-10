from turtle import *

ws = Screen()
ws.setup(width=550, height=400)

#turtle의 모양을 지정한다. 종류)arrow, turtle, circle, square, triangle, classic
shape('turtle') 
for s in range(4):
	left(90) # 각도를 90도 꺽는다
	forward(150)
	
done()


