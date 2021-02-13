import turtle

turtle.color('blue', )
turtle.width(2)
numbers_for_post_index = [x + 1 for x in range(0, 10) ]
turtle_rotation = [45, 90, 135, 180, 225, 270, 315, 360]
turtle_movement = [20, 50, 71, 100]


def start_point():
    """The function takes the turtle to the start point. """

    turtle.penup()
    turtle.backward(turtle_movement[3]*4)

def next_number ():
    """The function make backdown from the number. """

    turtle.penup()
    turtle.right(turtle_rotation[1])
    turtle.forward(turtle_movement[0])


def number_one():
    """The function draws one. """
   
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
    """The function draws two. """

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
    """The function draws three. """

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
    """The function draws four. """

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
    """The function draws five. """

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
    """The function draws six. """

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
    """The function draws seven. """

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
    """The function draws eight. """

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
    """The function draws nine. """

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
    """The function draws zero. """

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
    """
    The function asks the user for a number, 
    then draws the number that was entered by the user
    """

    start_point()
    general_number = str(input("Введіть число: "))
    general_number_list = list(general_number)
    number_pozition = -1
    for i in range (len(general_number)):
        number_pozition += 1

        if int(general_number_list[number_pozition]) == 1:
            number_one()
        elif int(general_number_list[number_pozition]) == 2:
            number_two()
        elif int(general_number_list[number_pozition]) == 3:
            number_three()
        elif int(general_number_list[number_pozition]) == 4:
            number_four()
        elif int(general_number_list[number_pozition]) == 5:
            number_five()
        elif int(general_number_list[number_pozition]) == 6:
            number_six()      
        elif int(general_number_list[number_pozition]) == 7:
            number_seven()
        elif int(general_number_list[number_pozition]) == 8:
            number_eight()    
        elif int(general_number_list[number_pozition]) == 9:
            number_nine()
        else:
            number_zero()    


post_index_maker()