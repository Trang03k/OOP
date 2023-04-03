


class Person:
    def __init__(self,first_name,last_name,date_of_birth):
        self.first_name = first_name
        self.last_name = last_name
        self.date_of_birth= date_of_birth

    def print_person_details(self):
        print(f'Name: {self.first_name} {self.last_name}')
        print(f'Date of Birth: {self.date_of_birth}')
        print(f'------------------------')

class Worker:
    def __init__(self, tax_file_number, super_number):
        self.tax_file_number = tax_file_number
        self.super_number = super_number

    def get_info(self):
        print(f'TFN: {self.tax_file_number}')
        print(f'Super: {self.super_number}')


class Employee2(Person,Worker):
    def __init__(self,first_name,last_name,date_of_birth,tax_file_number, super_number,employ_id,position):
        Person.__init__(self,first_name,last_name,date_of_birth)
        Worker.__init__(self,tax_file_number, super_number)
        self.employ_id = employ_id
        self.position = position

    def get_details(self):
        super().print_person_details()
        
        print(f'Employee ID: {self.employ_id}')
        print(f'Position: {self.position}')
        print(f'------------------------')

        super().get_info()




kim = Employee2('Kim', 'White', '12/08/2020', 4556655, 567,
1121, 'Developer')
print(kim.get_details())