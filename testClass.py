class Employee:
    def __init__(self, first, last, pay):  # same as constructor
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'

    def fullname(self):
        print('{} {}'.format(self.first, self.last))


emp_1 = Employee('Neil', 'Aspin', 65000)
emp_2 = Employee('Test', 'User', 50000)

print(emp_1)
print(emp_2)
# emp_1.first = 'Corey'
# emp_1.last = 'Shafer'
# emp_1.email = 'coreyshafer@gmail.com'
# emp_1.pay = 50000
#
# emp_2.first = 'Test'
# emp_2.last = 'User'
# emp_2.email = 'testuser@gmail.com'
# emp_2.pay = 60000

print(emp_1.email)
print(emp_2.email)

print('{} {}'.format(emp_2.first, emp_2.last))
print(emp_1.fullname())
print(emp_2.fullname())