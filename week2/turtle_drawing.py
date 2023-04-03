import turtle
myTurtle = turtle.Turtle()
myWindow = turtle.Screen()
myWindow.setup(width=600, height=500)
myWindow.bgcolor('beige')
myTurtle.pensize(3)
myTurtle.shape('turtle')
myTurtle.color('black')
myTurtle.penup()
myTurtle.goto(50, 100)
myTurtle.pendown()
myTurtle.forward(50)
myTurtle.right(90)
myTurtle.forward(100)

# Add code here to complete the rectangle
my_pos = myTurtle.pos()


myTurtle.forward(150)
myTurtle.right(90)
myTurtle.forward(100)
myTurtle.right(90)
myTurtle.forward(150)

myTurtle.color('green')


myTurtle.goto(my_pos)
myTurtle.forward(300)







myWindow.exitonclick()