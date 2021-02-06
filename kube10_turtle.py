import turtle
side_kube = 10
x, y = 0, 0
turtle.shape("turtle")

for i in range (10):
	turtle.penup()
	turtle.goto(x, y)
	turtle.pendown()
	for k in range (4):
		turtle.forward(side_kube)
		turtle.left(90)
	side_kube += 20
	x -= 10
	y -= 10
	