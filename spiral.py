# spiral graph:
import turtle

colors = ["blue", "purple"]

x = turtle.Turtle()

for i in range(30):
  x.color(colors[i%2])             # alternate between the colors
  x.circle(60)
  x.left(12)
