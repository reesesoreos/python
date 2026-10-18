import unittest

class Employee:
    def __init__(self, first, last, annual_salary):
        self.first = first
        self.last = last
        self.annual_salary = annual_salary
    
    def give_raise(self, raise_amount=5000):
        self.annual_salary = self.annual_salary + raise_amount


class TestEmployee(unittest.TestCase):
    def setUp(self):
        self.first = 'Jayden'
        self.last = 'Park'
        self.annual_salary = 60000
        self.person = Employee(self.first, self.last, self.annual_salary)
    
    def test_give_default_raise(self):
        self.person.give_raise()
        self.assertEqual(self.person.annual_salary, 65000)
    
    def test_give_custom_raise(self):
        self.person.give_raise(10000)
        self.assertEqual(self.person.annual_salary, 70000)

if __name__ == '__main__':
    unittest.main()