import turtle
terry = turtle.Turtle()
myWindow = turtle.Screen()



# Write your code here
myWindow.setup(width=750, height=500)
myWindow.bgcolor('beige')
my_pos = terry.pos()
terry.forward(150)
terry.left(120)
terry.right(180)
terry.forward(100)
terry.right(180)



terry.color('blue')

terry.goto(my_pos)
terry.forward(300)

myWindow.exitonclick()