###############################################
### SETUP ###
import turtle
###############################################

t=turtle.Turtle()

t.goto(100,-150)
t.color("white")
#speed set to 10
t.speed(10)

#set backround color to black
turtle.Screen().bgcolor("black")

#repeat 200 times
for i in range (200):
    t.left(1)
    t.forward(2)
t.right(120)

#repeat 200 times
for i in range (200):
    t.left(1)
    t.forward(2)
t.forward(224)
t.left(80)
t.forward(240)

turtle.exitonclick()