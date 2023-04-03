class Car:
    def __init__(self,topSpeed,speed):
        self.__topSpeed = topSpeed
        self.__speed = 0

    def setTopSpeed(self):
        if self.__topSpeed > 0:
            return self.__topSpeed
        else:
            raise ValueError(f'Invalid top speed {self.__topSpeed}')
    
    def getTopSpeed(self):
        return self.__topSpeed
    
    def getSpeed(self):
        return self.__speed
    
    def accelerate(self):
        self.__speed += 10
        if self.__speed > self.__topSpeed:
            self.__speed is self.__topSpeed
            raise ValueError(f'Cannot accelerate above top speed: {self.__topSpeed}')
    
    def decelerate(self):
        self.__speed -= 10
        if self.__speed < 0:
            self.__speed = 0
            raise ValueError('Cannot decelerate below zero')
        
    def __str__(self):
        return f'Car going {self.__topSpeed} kmph'
