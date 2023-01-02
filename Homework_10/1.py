class Student:
    def __init__(self, name='Ivan', age=18, group_number='10A'):
        self.name = name
        self.age = age
        self.groupNumber = group_number
 
    def get_name(self):
        return f'Name - {self.name}'
 
    def get_age(self):
        return f'Age - {self.age}'
 
    def get_group_number(self):
        return f'Group number - {self.groupNumber}.'
 
 
Anna = Student("Anna", 18, "09B")
print(f'{Anna.get_name()}, {Anna.get_age()}, {Anna.get_group_number()}')
