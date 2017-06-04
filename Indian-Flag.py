#############################################
#											#
#	By: Pradeep Gangwar 					#
#											#
#	https://pradeepgangwar.tech				#
#											#
#############################################

# Make sure you install Tkinter : **sudo apt-get install python-tk**



import turtle

def make_outer(pradeep):
	pradeep.setheading(90)
	pradeep.forward(100)
	pradeep.setheading(0)
	pradeep.forward(450)
	pradeep.setheading(270)
	pradeep.forward(100)
	pradeep.setheading(180)
	pradeep.forward(450)
	pradeep.end_fill()


def make_circle(pradeep):
	pradeep.up()
	pradeep.setpos(0,49)
	pradeep.down()
	pradeep.circle(49)

def make_spokes(pradeep):
	for i in range(1,25):
		pradeep.up()
		pradeep.setpos(0,0)
		pradeep.right(15)
		pradeep.down()
		pradeep.forward(49)

def make_stand(pradeep):
	pradeep.begin_fill()
	pradeep.up()
	pradeep.setpos(-225,150)
	pradeep.setheading(180)
	pradeep.down()
	pradeep.forward(20)
	pradeep.setheading(270)
	pradeep.forward(450)
	pradeep.setheading(0)
	pradeep.forward(20)
	pradeep.setheading(90)
	pradeep.forward(450)
	pradeep.end_fill()


def make_shape():
	window = turtle.Screen()
	window.bgcolor("white")
	window.setup(width=1.0, height=1.0, startx=None, starty=None)
	pradeep = turtle.Turtle()
	pradeep.shape("turtle")
	pradeep.color("black")
	pradeep.speed(1)

	pradeep.up()
	pradeep.setpos(-225,-150)
	pradeep.down()
	pradeep.color("green")
	pradeep.begin_fill()
	make_outer(pradeep)

	pradeep.up()
	pradeep.setpos(-225,-50)
	pradeep.down()
	pradeep.color("black")
	make_outer(pradeep)

	pradeep.up()
	pradeep.setpos(-225,50)
	pradeep.down()
	pradeep.color("#ff9933")
	pradeep.begin_fill()
	make_outer(pradeep)

	pradeep.color("black")
	make_circle(pradeep)
	make_spokes(pradeep)
	make_stand(pradeep)
	pradeep.up()
	pradeep.setpos(250,200)

	window.exitonclick()

make_shape()