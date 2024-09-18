class User:#класс без инициализатора - при создании объекта параметры не используется 
    name = 'None'
    age = ''
    password = ''
    login = ''
    
    def get(self):
        return self.name
        

user = User()
print(user.name)
print(user.password)
user.password = '1234qwerty'
print(user.get())
print(user.password)

class Student:
    def __init__(self, groups):
        self._groups = groups
    @property
    def groups(self):
        return self._groups
        

student = Student('22ИСиП')
print(student.groups)            