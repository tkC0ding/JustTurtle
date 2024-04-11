import turtle
t = turtle.Turtle()
while(True):
	t.home()
	t.speed(1) # 1:slowest, 3:slow, 5:normal, 10:fast, 0:fastest
	t.penup()
	t.setheading(180)
	t.forward(200)

	t.setheading(0)
	t.pendown()
	t.circle(100, 180)
	t.setheading(270)
	t.forward(200)
	t.setheading(0)

	t.penup()

	t.forward(150)
	t.setheading(90)
	t.pendown()
	t.forward(200)
	t.setheading(300)
	t.forward(225)
	t.setheading(90)
	t.forward(200)
	t.setheading(0)

	t.penup()

	t.forward(50)
	t.pendown()
	t.forward(150)
	t.penup()
	t.setheading(180)
	t.forward(75)
	t.setheading(270)
	t.pendown()
	t.forward(200)
	t.penup()