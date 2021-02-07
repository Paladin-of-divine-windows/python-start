from random import *
import turtle

def random_turtle ():
    for i in range (100):
         turtle.forward(randint(1, 100))
         turtle.right(randint(0, 360))
         turtle.backward(randint(1, 100))
         turtle.left(randint(0, 360))
         turtle.forward(random())

random_turtle()

