class MovingObject:
    def __init__(self,speed,mass):
        self.speed = speed
        self.mass = mass

    def distance(self,time):
        return self.speed *time
    
    def kinetic_energy(self,velocity):
        return self.mass*1/2*(velocity**2)
    
mv = MovingObject(60,10)
print(mv.distance(100))
print(mv.kinetic_energy(60))
        
