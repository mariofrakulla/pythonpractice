""" Examples of Multiple Inheritance in Python """
""" inheriting from two classes at the same time """

class Student:
    def __init__(self, r, n):
        self.roll = r
        self.name = n
    def showStudent(self):
        print('Roll: ', self.roll)
        print('Name: ', self.name)

class Science:
    def __init__(self,sub_one, sub_two):
        self.Physics = sub_one
        self.Chemistry = sub_two
    def showScience(self):
        print('Physics: ', self.Physics)
        print('Chemistry: ', self.Chemistry)

class Results(Student, Science):
    def __init__(self, r, n, sub_one, sub_two):
        Student.__init__(self, r, n)
        Science.__init__(self, sub_one, sub_two)
        self.total = sub_one + sub_two
        self.average = self.total/2
    def showResults(self):
        Student.showStudent(self)
        Science.showScience(self)
        print('Total Score: ', self.total)
        print('Average Score: ', self.average)

res_one = Results('231', 'Mario', 100,100)
res_one.showResults()

""" Two Base classes having a method with the same name and signature """

class Rectangle:
    def __init__(self):
        self.x = 7
        self.y = 13
    def area(self):
        self.Area = self.x *self.y
class Triangle:
    def __init__(self):
        self.a = 7
        self.b = 12
    def area(self):
        self.Area = 0.5*self.a * self.b

class both(Rectangle,Triangle):
    pass


r = both()
print('Area is: ', r.area())

