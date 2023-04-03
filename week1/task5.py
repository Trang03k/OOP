class MovingObject:
    def __init__(self,speed,mass):
        self.speed = speed
        self.mass = mass

    def distance(self,time):
        return self.speed *time
    
mv= MovingObject(6,20)
print(mv.distance(21))