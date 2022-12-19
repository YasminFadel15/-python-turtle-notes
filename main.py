import turtle

t = turtle.Turtle()
turtle.Turtle()

# commands:
t.forward()
t.right()
t.left()
t.seth()                           # change the direction
t.penup()                          # unglued the marker 
t.spedd()
t.back()

# create a triangle:
for i in range(3):
  t.forward(15)                    # moves the turtle the direction it's facing how ever pixels in ()
  t.left(120)        

# create a circle, the radians in ():
t.circle(30)         

# create a rectangle:
for i in range(2):
  t.forward(30)     
  t.left(90) 
  t.forward(15)
  t.left(90)

# change the color:
t.color("red")                     # or t.pencolor("red"), change the color of the marker
t.fillcolor("red")                 # fill the color in a shape
t.begin_fill()                     # before start the shape
t.end_fill()                       # after created the shape

# example:
t.fillcolor("red")
t.begin_fill
for i in range(4):
  t.forward(20)
  t.left(90)
t.end_fill()

# change the size:
t.pensize(10)                      # change the marker's size
