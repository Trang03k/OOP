class Car:
    def __init__(self,topSpeed,speed):
        self.__topSpeed = topSpeed
        self.__speed = 0

    def setTopSpeed(self):
        if self.__topSpeed > 0:
            return self.__topSpeed
        else:
            raise ValueError(f'Invalid top speed {self.__topSpeed}')
    