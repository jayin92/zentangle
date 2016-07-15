import turtle
import math
import time

degree = 0.1
tri = 500
hi = []
bi = []
ai = []

turtle.speed(-1)
turtle.color('black','white')
turtle.pensize(0.5)
turtle.begin_fill()
turtle.penup()
turtle.goto(-250,250)
turtle.pendown()

for i in range(4):
	turtle.forward(tri)
	turtle.right(90)	
turtle.end_fill()

for i in range(100000) :
	if i < 3:
		if i == 0:
			b = tri
		else:				
			b = tri - ai[i-1] 
		turtle.right(degree)		
		h = b / math.cos(math.radians(degree))		 
		a = math.tan(math.radians(degree)) * b			
		turtle.forward(h)
		hi.append(h)
		bi.append(b)
		ai.append(a)				 
		turtle.right(90-degree)		

	if i % 4 == 3: 
		if i == 3:
			h = tri - ai[2]
		else:
			h = bi[i-4] - ai[i-1]
		turtle.right(degree)
		a = math.sin(math.radians(degree)) * h
		b = math.cos(math.radians(degree)) * h
		turtle.forward(b)		
		hi.append(h)
		bi.append(b)
		ai.append(a)  
		turtle.right(90+degree)

	if i > 3 & i % 4 != 3:
		b = hi[i-4]	- ai[i-1]	
		h = b / math.cos(math.radians(degree))
		a = math.tan(math.radians(degree)) * b
		turtle.forward(h)
		hi.append(h)
		bi.append(b)
		ai.append(a)		
		turtle.right(90)
		if i > 3 & i % 4 == 2:
			turtle.left(degree)

	print(i)

turtle.exitonclick()