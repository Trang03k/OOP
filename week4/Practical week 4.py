#task 1
class Person:
    def __init__(self,name,age,money):
        self.__name = name
        self.__age = age
        self._money = money 
        self.__Alive = True
    
    def getName(self):
        return self.__name
    
    def getAge(self):
        return self.__age
    
    def isAlive(self):
        return self.__Alive
    
    def getMoney(self):
        return self._money
    
    def setName(self,name):
        self.__name = name
    
    def haveBirthday(self):
        self.__age += 1
    
    def spendMoney (self,amount):
        if amount <= self._money:
            self._money -= amount
        else:
            print('Error: Cannot spend that much money')
    
    def die(self):
        self.__Alive = False
girl = Person('Tiffany', 22, 5000.50)
print(girl.getName())
print(girl.getAge())
print(girl.isAlive())
print(girl.getMoney())

girl.setName('Rose')
print(girl.getName())

girl.haveBirthday()
print(girl.getAge())

girl.spendMoney(3000)
print(girl.getMoney())

girl.die()
print(girl.isAlive())


#task2

class Employee(Person):
    def __init__(self, name, age, money,jobTitle,wage,):
        super().__init__(name, age, money)
        self.__jobTitle = jobTitle
        self.__wage = wage
        self.__hours = 0
    
    def getJobTitle(self):
        return self.__jobTitle 
    
    def setWage(self,wage):
        if wage > 0:
            self.__wage = wage
    
    def work(self,numHourse):
        self.__hours += numHourse

    def receivePay(self):
        salary = self.__hours * self.__wage 
        self._money += salary
        self.__hours = 0

ada = Employee('Ada', 36, 3000, 'mathematician', 40)
print(ada.getJobTitle())
ada.work(8)
ada.receivePay()
print('$' + str(ada.getMoney()))
ada.setWage(100)
ada.work(8)
ada.receivePay()
print('$'+ str(ada.getMoney()))
ada.die()


#task3
import random
class Programmer(Employee):
    example = ["print('hello world')", "x=0", "raise Exception('What am I doing??')"]
    def __init__(self, name, age, money, wage):
        super().__init__(name, age, money, 'Programmer', wage)
        
    def createCode(self):
        return random.choice(Programmer.example)
    def work(self,numHours):
        super().work(numHours)
        for num in range(numHours):
            code = self.createCode()
            print(f"Hour {num+1} - Code Created: {code}")



job = Programmer('Tiffany', 22, 5000.50, 50.0)
print(job.getName) 
print(job.getAge()) 
print(job.getMoney())
print(job.getJobTitle()) 

job.work(18)

job.receivePay() 
print(job.getMoney()) 

 
job.spendMoney(5000.0) 
print(job.getMoney())







