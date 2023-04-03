
#Task 1
class Car:
    def __init__(self,topSpeed):
        self.__topSpeed = topSpeed
        self.setTopSpeed(topSpeed)
        self.__speed = 0

    def setTopSpeed(self,topSpeed):
        if self.__topSpeed > 0:
            self.__topSpeed = topSpeed
        else:
            raise Exception(f'Invalid top speed {self.__topSpeed}')
    
    def getTopSpeed(self):
        return self.__topSpeed
    
    def getSpeed(self):
        return self.__speed
    
    def accelerate(self):
        self.__speed += 10
        if self.__speed > self.__topSpeed:
            self.__speed = self.__topSpeed
            raise Exception(f'Cannot accelerate above top speed: {self.__topSpeed}')
    
    def decelerate(self):
        self.__speed -= 10
        if self.__speed < 0:
            self.__speed = 0
            raise Exception('Cannot decelerate below zero')
        
    def __str__(self):
        return f'Car going {self.__speed}/{self.__topSpeed} kmph'


#Task2

#1
car1 = Car(250)
print(car1)
#2
#car2 = Car(-99)
#print(car2)

#3
try:
    car2 = Car(-99)
    print(car2)
except:
    print('I caught an exception')

#4
#for i in range(30):
#    car1.accelerate()
#    print(car1)

#5
try:
    for i in range(30):
        car1.accelerate()
        print(car1)
except:
    print('I caught an exception')

#6
#for i in range(30):
#    car1.decelerate()
#    print(car1)

#7
for i in range(30):
    try: 
        car1.decelerate()
        print(car1)
    except:
        print('I caught an exception ')

#8
try:
    topspeed = Car(float(input('Please enter a number:')))
except: 
    print('I caught an exception ')



