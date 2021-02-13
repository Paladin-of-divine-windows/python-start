import turtle

turtle.color('blue', )
turtle.width(2)
numbers_for_post_index = [x + 1 for x in range(0, 10) ]
turtle_rotation = [45, 90, 135, 180, 225, 270, 315, 360]
turtle_movement = [20, 50, 71, 100]


def start_pozition():
    turtle.penup()
    turtle.backward(turtle_movement[3]*4)

def next_number ():
    turtle.penup()
    turtle.right(turtle_rotation[1])
    turtle.forward(turtle_movement[0])


def number_one():
    '''The function draws one. '''
   
    turtle.penup()
    turtle.forward(turtle_movement[1])
    turtle.pendown()
    turtle.right(turtle_rotation[1])
    turtle.forward(turtle_movement[3])
    turtle.right(turtle_rotation[3])
    turtle.forward(turtle_movement[3])
    turtle.left(turtle_rotation[2])
    turtle.forward(turtle_movement[2])
    turtle.left(turtle_rotation[2])
    turtle.penup()
    turtle.forward(turtle_movement[1])
    turtle.left(turtle_rotation[1])
    turtle.forward(turtle_movement[1])
    next_number()


def number_two():
    turtle.pendown()
    turtle.forward(turtle_movement[1])
    turtle.right(turtle_rotation[1])
    turtle.forward(turtle_movement[1])
    turtle.right(turtle_rotation[0])
    turtle.forward(turtle_movement[2])
    turtle.left(turtle_rotation[2])
    turtle.forward(turtle_movement[1])
    turtle.penup()
    turtle.left(turtle_rotation[1])
    turtle.forward(turtle_movement[3])
    next_number()


def number_three():
    turtle.pendown()
    turtle.forward(turtle_movement[1])
    turtle.right(turtle_rotation[2])
    turtle.forward(turtle_movement[2])
    turtle.left(turtle_rotation[2])
    turtle.forward(turtle_movement[1])
    turtle.right(turtle_rotation[2])
    turtle.forward(turtle_movement[2])
    turtle.penup()
    turtle.left(turtle_rotation[2])
    turtle.forward(turtle_movement[1])
    turtle.left(turtle_rotation[1])
    turtle.forward(turtle_movement[3])
    next_number()


def number_four():
    turtle.pendown()
    turtle.right(turtle_rotation[1])
    turtle.forward(turtle_movement[1])
    turtle.left(turtle_rotation[1])
    turtle.forward(turtle_movement[1])
    turtle.right(turtle_rotation[1])
    turtle.forward(turtle_movement[1])
    turtle.left(turtle_rotation[3])
    turtle.forward(turtle_movement[3])
    next_number()


def number_five():
    turtle.pendown()
    turtle.forward(turtle_movement[1])
    turtle.backward(turtle_movement[1])
    turtle.right(turtle_rotation[1])
    turtle.forward(turtle_movement[1])
    turtle.left(turtle_rotation[1])
    turtle.forward(turtle_movement[1])
    turtle.right(turtle_rotation[1])
    turtle.forward(turtle_movement[1])
    turtle.left(turtle_rotation[1])
    turtle.backward(turtle_movement[1])
    turtle.forward(turtle_movement[1])
    turtle.penup()
    turtle.left(turtle_rotation[1])
    turtle.forward(turtle_movement[3])
    next_number()


def number_six():
    turtle.penup()
    turtle.right(turtle_rotation[1])
    turtle.forward(turtle_movement[1])
    turtle.pendown()
    turtle.forward(turtle_movement[1])
    turtle.left(turtle_rotation[1])
    turtle.forward(turtle_movement[1])
    turtle.left(turtle_rotation[1])
    turtle.forward(turtle_movement[1])
    turtle.left(turtle_rotation[1])
    turtle.forward(turtle_movement[1])
    turtle.right(turtle_rotation[2])
    turtle.forward(turtle_movement[2])
    turtle.left(turtle_rotation[0])
    next_number()  


def number_seven():
    turtle.pendown()
    turtle.forward(turtle_movement[1])
    turtle.right(turtle_rotation[2])
    turtle.forward(turtle_movement[2])
    turtle.left(turtle_rotation[0])
    turtle.forward(turtle_movement[1])
    turtle.penup()
    turtle.left(turtle_rotation[1])
    turtle.forward(turtle_movement[1])
    turtle.left(turtle_rotation[1])
    turtle.forward(turtle_movement[3])
    next_number()


def number_eight():
    turtle.pendown()
    turtle.forward(turtle_movement[1])
    turtle.backward(turtle_movement[1])
    turtle.right(turtle_rotation[1])
    turtle.forward(turtle_movement[3])
    turtle.left(turtle_rotation[1])
    turtle.forward(turtle_movement[1])
    turtle.left(turtle_rotation[1])
    turtle.forward(turtle_movement[1])
    turtle.left(turtle_rotation[1])
    turtle.forward(turtle_movement[1])
    turtle.backward(turtle_movement[1])
    turtle.right(turtle_rotation[1])
    turtle.forward(turtle_movement[1])
    next_number()


def number_nine():
    turtle.pendown()
    turtle.forward(turtle_movement[1])
    turtle.backward(turtle_movement[1])
    turtle.right(turtle_rotation[1])
    turtle.forward(turtle_movement[1])
    turtle.left(turtle_rotation[1])
    turtle.forward(turtle_movement[1])
    turtle.right(turtle_rotation[2])
    turtle.forward(turtle_movement[2])
    turtle.penup()
    turtle.left(turtle_rotation[2])
    turtle.forward(turtle_movement[1])
    turtle.left(turtle_rotation[1])
    turtle.forward(turtle_movement[1])
    turtle.pendown()
    turtle.forward(turtle_movement[1])
    next_number()


def number_zero():
    turtle.pendown()
    turtle.forward(turtle_movement[1])
    turtle.backward(turtle_movement[1])
    turtle.right(turtle_rotation[1])
    turtle.forward(turtle_movement[3])
    turtle.left(turtle_rotation[1])
    turtle.forward(turtle_movement[1])
    turtle.left(turtle_rotation[1])
    turtle.forward(turtle_movement[3])
    next_number()


def post_index_maker():
    number_zero()
    number_six()
    number_nine()
    number_two()


start_pozition()
post_index_maker()
turtle.penup()
turtle.forward(1000)