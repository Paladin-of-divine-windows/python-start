import turtle
distance = 10

turtle.shape("turtle")

for x in range (1, 50):

	if x % 2 == 0:
		distance += 10

	turtle.forward(distance)
	turtle.left(90)
