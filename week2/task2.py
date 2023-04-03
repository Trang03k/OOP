import turtle
import random
myTurtle = turtle.Turtle()
myWindow = turtle.Screen()
myWindow.setup(width=800, height=800)
myWindow.bgcolor('beige')
class TurtleCluster:
    def __init__(self):
        self.cluster = []

    def addTurtle(self,turtle):
        self.cluster.append(turtle)

    def goToLocation(self,x,y):
        for t in self.cluster:
            t.goto(x,y)
            turtle.forward(x)
            turtle.left(y)
            
        # for i in range(3):
        #     turtle.forward(x)
        #     turtle.left(y)
            
    
    def spreadOut(self, radius,step):
        for t in (self.cluster):
            t.right(random.randint(1,360))
            t.forward(random.randint(20, 50))

            # turtle.circle(radius)
            # turtle.forward(step)
            


my_cluster = TurtleCluster()
for i in range(4):
    my_cluster.addTurtle(turtle.Turtle())

for i in range(5):
    my_cluster.goToLocation(x=150,y= 60)
    
    my_cluster.spreadOut(random.randint(1,360),random.randint(1,100))
    my_cluster.goToLocation(x=150,y= 150
                            )

    

my_cluster.addTurtle(turtle.Turtle())

           
myWindow.exitonclick()
        