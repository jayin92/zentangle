import turtle
import math
import time



hi = []
bi = []
ai = []
area = 0

mode = turtle.numinput("選擇模式", "模式 1 為 無限模式  模式 2 為有限模式", 2, minval = 1, maxval = 2)
degree = turtle.numinput("選擇角度", "0 < 角度 <= 45", 15, minval = 10 ** -10, maxval = 45)
tri = turtle.numinput("選擇正方形邊長", "0 < 邊長", 250, minval = 10 ** -10, maxval = 10 ** 10)
turtle.speed(-1)
turtle.color('black','white')
turtle.pensize(0.5)
turtle.begin_fill()
turtle.penup()
turtle.goto(-(tri / 2),(tri / 2))
turtle.pendown()
turtle.hideturtle()

for i in range(4):
	turtle.forward(tri)
	turtle.right(90)	
turtle.end_fill()

i = 0

while True:	
	if i < 3:
		if i == 0:
			b = tri
		else:				
			b = tri - ai[i-1] 
		turtle.right(degree)		
		h = b / math.cos(math.radians(degree))		 
		a = math.tan(math.radians(degree)) * b
		area = (a * b) / 2 + area 
		if tri * tri - area < 0 and mode == 2:
			break
		turtle.forward(h)
		print("The value of i now is ",i)
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
		area = (a * b) / 2 + area
		if tri * tri - area < 0 and mode == 2:
			break		
		turtle.forward(b)
		print("The value of i now is ",i)
		hi.append(h)
		bi.append(b)
		ai.append(a)  
		turtle.right(90+degree)

	if i > 3 & i % 4 != 3:
		b = hi[i-4]	- ai[i-1]	
		h = b / math.cos(math.radians(degree))
		a = math.tan(math.radians(degree)) * b	
		area = (a * b) / 2 + area 
		if tri * tri - area < 0 and mode == 2:
			break	
		turtle.forward(h)
		print("The value of i now is ",i)
		hi.append(h)
		bi.append(b)
		ai.append(a)		
		turtle.right(90)
		if i > 3 & i % 4 == 2:
			turtle.left(degree)
	i += 1

turtle.exitonclick()