""" Examples """
""" Multi Level Inheritance --> Two classes inheriting
    from the same class """

class Worker:
    def __init__(self, c, n, s):
        self.code = c
        self.name = n
        self.salary = s

    def showWorker(self):
        print('Code: ', self.code)
        print('Name: ', self.name)
        print('Salary: ', self.salary)

class Officer(Worker):
    def __init__(self, c, n, s):
        Worker.__init__(self, c, n, s)
        self.hra = s/10
    def showOfficer(self):
        Worker.showWorker(self)
        print('HRA: ', self.hra)
        print('\n')
class Manager(Officer):
    def __init__(self, c, n, s):
        Worker.__init__(self,c,n,s)
        self.hra = s/10
        self.da = s/12
    def showManager(self):
        Worker.showWorker(self)
        print('HRA: ', self.hra)
        print('DA : ', self.da)
        print('\n')

worker_one = Worker(1234, 'Mario', 75000)
worker_one.showWorker()
officer_one = Officer(1234, 'Mario', 90000)
officer_one.showOfficer()
manager_one = Manager(1234, 'Mario', 125000)
manager_one.showManager()

""" Science -> Student <- Arts """

class Student:
    def __init__(self,r,n):
        self.roll = r
        self.name = n
    def showStudent(self):
        print('Roll: ', self.roll)
        print('Name: ', self.name)

class Science(Student):
    def __init__(self,r,n,s_one, s_two):
        Student.__init__(self,r,n)
        self.physics = s_one
        self.chemistry = s_two

    def showScience(self):
        print('\n')
        Student.showStudent(self)
        print('Subject One: ', self.physics)
        print('Subject Two: ', self.chemistry)
class Arts(Student):
    def __init__(self,r,n,s_one, s_two):
        Student.__init__(self,r,n)
        self.history = s_one
        self.geography = s_two
    def showArts(self):
        print('\n')
        Student.showStudent(self)
        print('Subject one: ', self.history)
        print('Subject two: ', self.geography)

studentOne = Student('Honors', 'Mario')
studentOne.showStudent()
studentScience = Science('Honors', 'Mario', 100, 100)
studentScience.showScience()
arts_student = Arts('Honors', 'Name', 100, 100)
arts_student.showArts()




