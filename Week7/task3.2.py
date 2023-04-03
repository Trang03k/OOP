class NoDriverException(Exception):
    def __init__(self):
        super().__init__('Cannot drive without a Driver')


class SpeedException(Exception):
    pass

class Car:
    def __init__(self,topSpeed):
        self.__topSpeed = topSpeed
        self.setTopSpeed(topSpeed)
        self.__speed = 0
        self.__driver = None

    def setTopSpeed(self,topSpeed):
        if self.__topSpeed > 0:
            self.__topSpeed = topSpeed
        else:
            raise SpeedException(f'Invalid top speed {self.__topSpeed}')
    
    def getTopSpeed(self):
        return self.__topSpeed
    
    def getSpeed(self):
        return self.__speed
    
    def setDriver(self,driver):
        self.__driver = driver
    
    def accelerate(self):
        self.__speed += 10
        if self.__speed > self.__topSpeed:
            self.__speed = self.__topSpeed
            raise SpeedException(f'Cannot accelerate above top speed: {self.__topSpeed}')
        if self.__driver is None:
            raise NoDriverException()
    
    def decelerate(self):
        self.__speed -= 10
        if self.__speed < 0:
            self.__speed = 0
            raise SpeedException('Cannot decelerate below zero')
        if self.__driver is None:
            raise NoDriverException()
    def __str__(self):
        return f'Car going {self.__speed}/{self.__topSpeed} kmph'
    


car1 = Car(250)
car1.setDriver('Valentino')
print(car1)

try:
    car2 = Car(-99)
    print(car2)
except:
    print('I caught an exception')

try:
    for i in range(30):
        car1.accelerate()
        print(car1)
except:
    print('I caught an exception')

