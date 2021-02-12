import turtle

turtle.color('blue', )
turtle.width(2)
numbers_for_post_index = [x + 1 for x in range(0, 10) ]
turtle_rotation = [45, 90, 135, 180, 225, 270, 315, 360]
turtle_movement = [20, 50, 71, 100]


def number_one(movment, rotation):
    '''The function draws one. '''
    
    turtle.left(turtle_rotation[0])
    turtle.forward(turtle_movement[2])
    turtle.right(turtle_rotation[2])
    turtle.forward(turtle_movement[3])
    turtle.right(turtle_rotation[3])
    turtle.forward(turtle_movement[3])
    turtle.penup()
    turtle.right(turtle_rotation[1])
    turtle.forward(turtle_movement[0])


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
    turtle.right(turtle_rotation[1])
    turtle.forward(turtle_movement[0])



def number_three():
    pass


def number_four():
    pass


def number_five():
    pass


def number_six():
    pass


def number_seven():
    pass


def number_eight():
    pass


def number_nine():
    pass


def number_zero():
    pass


def post_index_maker():
    number_one(turtle_movement, turtle_rotation)
    number_two()

post_index_maker()
turtle.penup()
turtle.forward(1000)