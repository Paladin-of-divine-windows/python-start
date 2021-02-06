import turtle

 
angles = 3
leng = 0


def polygon (angles, leng):


	for i in range(angles):
		turtle.forward(100 + leng)
		turtle.right(360 / angles)
		

def repits(angles, leng):
	
	angles += 1
	leng += 20
	turtle.penup()
	turtle.backward(leng/2)
	turtle.right(90)
	turtle.backward(leng/2)
	turtle.left(90)
	turtle.forward(leng/2)
	turtle.pendown()
		

polygon(angles, leng - 10)
turtle.penup()
turtle.backward(7)
turtle.right(90)
turtle.backward(7)
turtle.left(90)
turtle.pendown()

for i in range(1,10):

	polygon(angles + 1, leng)
	repits(angles, leng)
	angles += 1


#turtle.penup()
#turtle.forward(1000000)