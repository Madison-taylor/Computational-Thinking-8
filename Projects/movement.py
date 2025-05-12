# Section 1 - Helper functions (DON'T CHANGE!!)
import turtle, math, time, random
def set_background(image_filename):
	screen = turtle.Screen()
	try:
		screen.bgpic(f"/workspaces/Computational-Thinking-8/Backgrounds/{image_filename}.png")
	except:
		screen.bgpic(f"/workspaces/Computational-Thinking-8/Backgrounds/{image_filename}.gif")
def set_image(sprite, image_filename):
	image_file = f"/workspaces/Computational-Thinking-8/Images/{image_filename}.gif"
	screen = turtle.Screen()
	screen.register_shape(image_file)
	sprite.shape(image_file)
def create_sprite(image_filename, x=0, y=0):
	sprite = turtle.Turtle()
	set_image(sprite, image_filename)
	sprite.penup()
	sprite.goto(x,y)
	return sprite
def get_distance(s1, s2):
	dx = s1.xcor() - s2.xcor()
	dy = s1.ycor() - s2.ycor()
	return math.sqrt(dx*dx + dy*dy)
window = turtle.Screen()
window.tracer(0)


### SECTION_2:_Setup ###
set_background("castle")
s1 = create_sprite("jelly cat bunny",0,-200)
s2 = create_sprite("jelly cat teddy bear",0,-200)
s3 = create_sprite("fish",0,-200)
s4 = create_sprite("fish",0,-200)
s5 = create_sprite("fish",0,-200)
s6 = create_sprite("fish",0,-200)
s7 = create_sprite("fish",0,-200)
s8 = create_sprite("fish",0,-200)

### SECTION_2:_DEFINE_MOVEMENT_CONTROLS ###
def bunny_move_up():
    s1.setheading(90)
    s1.forward(10)
     
def bunny_move_down():
    s1.setheading(270)
    s1.forward(10)
    
def bunny_move_left():
    s1.setheading(180)
    s1.forward(10)
    
def bunny_move_right():    
    s1.setheading(0)
    s1.forward(10)

def bear_move_up():
    s2.setheading(90)
    s2.forward(10)
     
def bear_move_down():
    s1.setheading(270)
    s2.forward(10)    

def bear_move_left():
    s2.setheading(180)
    s2.forward(10)
    
def bear_move_right():    
    s2.setheading(0)
    s2.forward(10)



## APPLY_DEFINITIONS_OF_MOVEMENT ###

window.onkeypress(bunny_move_up, "Up")
window.onkeypress(bunny_move_down, "Down")
window.onkeypress(bunny_move_right, "Right")
window.onkeypress(bunny_move_left, "Left")

window.onkeypress(bear_move_up, "w")
window.onkeypress(bear_move_down, "s")
window.onkeypress(bear_move_right, "d")
window.onkeypress(bear_move_left, "a")

# Section 4: Game Loop
window.listen()
timer = 0
while True:
	time.sleep(0.1)
	timer += 1  
	 
    
 	# TODO - code for automatic actions






	window.update()

	# if :
	# 	break
	

print("Game Over")