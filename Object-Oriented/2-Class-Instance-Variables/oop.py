
class Employee:
    
    raise_amount = 1.04             # Class Variable #
    num_of_emps = 0                 # Class Variable #
    
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.email = first + '.' + last + '@email.com'
        self.pay = pay

    def fullname(self):
        return '{} {}'.format(self.first, self.last)
    
    def apply_raise(self):
        self.pay = int(self.pay * Employee.raise_amount)
        #self.pay = int(self.pay * self.raise_amount)
  

emp_1 = Employee('Corey', 'Schafer', 50000)
emp_2 = Employee('Test', 'Employee', 60000)

print emp_1.pay
emp_1.apply_raise()
print emp_1.pay
