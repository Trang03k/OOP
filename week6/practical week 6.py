import abc
class PaidEmployee(metaclass=abc.ABCMeta):
  @abc.abstractmethod
  def get_salary(self):
    pass
  @abc.abstractmethod
  def get_staff_info(self):
    pass
  
#instantiate
#create an instance/object
#object = PaidEmployee()
#print(object)
  
class Employee(metaclass=abc.ABCMeta):
  def __init__(self, first_name, last_name, employee_id):
    self.first_name = first_name
    self.last_name = last_name
    self.employee_id = employee_id
    self.base_salary = 0

  def set_base_salary(self, salary):
    self.base_salary = salary
  

  @abc.abstractmethod
  def get_salary(self):
    pass

  @abc.abstractmethod

  def get_staff_info(self):
    pass

class TeachingStaff (Employee):
  def __init__(self, first_name, last_name, employee_id, teaching_area, category):
    super().__init__(first_name, last_name, employee_id)
    self.teaching_area = teaching_area
    if category>=1 and category<=5:
      self.category = category
    else:
      # The following print statement was not a requirement:
      print("Error: The category of a teaching staff should be between 1 and 5.")
      self.category = 0
    
  def get_salary(self):
    salary = (((self.category * 10) + 100)/100) * self.base_salary
    return salary
  
  def get_staff_info(self):
    return 'First name: ' + self.first_name + \
    '\nLast name: ' + self.last_name + \
    '\nEmployee ID: ' + str(self.employee_id) + \
    '\nArea of Expertise: ' + self.teaching_area + \
    '\nCategory: ' + str(self.category) + \
    '\nSalary: ' + str(self.get_salary())

class AdministrativeStaff(Employee):
  def __init__(self, first_name, last_name, employee_id, level):
    super().__init__(first_name, last_name, employee_id)
    
    if level>=1 and level<=3:
      self.level = level
    else:
      # The following print statement was not a requirement:
      print("Error: The level of an administrative staff should be between 1 and 3.")
      self.level = 0

  def get_salary(self):
    salary = (((self.level * 15) + 100)/100) * self.base_salary
    return salary

  def get_staff_info(self):
    return 'First name: ' + self.first_name + \
    '\nLast name: ' + self.last_name + \
    '\nEmployee ID: ' + str(self.employee_id) + \
    '\nLevel: ' + str(self.level) + \
    '\nSalary: ' + str(self.get_salary())


employee= TeachingStaff('Kim', 'White',4532,'NY',4 )
employee.set_base_salary(4000)
print(employee.get_salary())

