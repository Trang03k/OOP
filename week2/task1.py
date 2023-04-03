import turtle
myTurtle = turtle.Turtle()
myWindow = turtle.Screen()



# Write your code here
my_pos = myTurtle.pos()


myTurtle.forward(100)
myTurtle.right(90)
myTurtle.forward(100)
myTurtle.right(135)
myTurtle.forward(180)

myTurtle.goto(my_pos)
myTurtle.forward(300)

myWindow.exitonclick()