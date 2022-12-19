# TURTLE MOTION
# move and draw
forward() | fd()
backward() | bk() | back()
right() | rt()
left() | lt()
goto(x, y) | setpos() | setposition()      # move turtle to an absolute position, don't change the orientation
setx()
sety()
setheading(to_angle) | seth()              # set the orientation of the turtle to to_angle
home()                                     # move turtle to the origin
circle()
dot(size, *color)
stamp()                                    # stamp a copy of the turtle position onto the canvas as the current turtle position
clearstamp(stampid)                        # delete stamp with given stampid
clearstamps(n)                             # clear n stamps
undo()                                     # undo the last turtle action
speed()

# tell turtle's state
position() | pos()                         # return the turtle's current location
towards()                                  # return the angle between the line from turtle position to position specified by (x,y), the vector or the other turtle
xcor()
ycor()
heading()
distance()

#setting and measurement
degrees()
radians()

# PEN CONTROL
# drawing state
pendown() | pd() | down()
penup() | pu() | up()
pensize() | width()
pen()
isdown()

# color control
color()
pencolor()
fillcolor()

# filling
filling()
begin_fill()
end_fill()

# more drawing control
reset()
clear()
write()

# TURTLE STATE
# visibility
showturtle() | st()
hideturtle() | ht()
isvisible()

# appearance
shape()
resizemode()
shapesize() | turtlesize()
shearfactor()
settiltangle()
tiltangle()
tilt()
shapetransform()
get_shapepoly()

# using events
onclick()
onrelease()
ondrag()

# special Turtle methods
begin_poly()
end_poly()
get_poly()
clone()
getturtle() | getpen()
getscreen()
setundobuffer()
undobufferentries()

# METHODS OS TURTLE SCREEN / SCREEN
# window control
bgcolor()
bgpic()
clearscreen()
resetscreen()
screensize()
setworldcoordinates()

# animation control
delay()
tracer()
update()

# using screen events
listen()
onkey() | onkeyrelease()
onkeypress()
onclick() | onscreenclick()
ontimer()
mainloop() | done()

# settings and special methods
mode()
colormode()
getcanvas()
getshapes()
register_shape() | addshape()
turtles()
window_height()
window_width()

# input methods
textinput()
numinput()

# methods specific to Screen
bye()
exitonclick()
setup()
title()

