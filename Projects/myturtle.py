###############################################
### SETUP ###
import turtle
###############################################

t=turtle.Turtle()
t.penup()
t.goto(-100,-100)
t.color("green")
t.pendown()

# repeat these next two lines 1 times
for i in range (3):
    t.forward(50)
    t.left(90)
  

###############################################
### ENDING ###
turtle.exitonclick()
###############################################