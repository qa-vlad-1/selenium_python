# OOP
class student():

    amount_raised = 1.04
    def __init__(self, first, last, salary):
        self.first = first
        self.last = last
        self.salary = salary

    def fullname(self):
        self.email = self.first + self.last + "@yahoo.com"
        return '{} {} {} {}'.format(self.first, self.last, self.salary, self.email)

    def annual_salary(self):
        self.salary = int(self.salary * self.amount_raised)
        print(self.salary)

emp_1 = student("Vlad", "Kal", 45000)
emp_2 = student("Tim", "Mayor", 100000)
print(emp_1.salary)
emp_1.annual_salary()
print(emp_1.amount_raised)



