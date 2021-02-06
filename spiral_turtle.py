import turtle
distance = 0.5

turtle.shape("turtle")

for x in range (1, 150):

	if x % 2 == 0:
		distance += 0.5

	turtle.forward(distance)
	turtle.left(30)