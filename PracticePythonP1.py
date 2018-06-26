""" Problem I, Practice Python
Create a program that asks the user to enter their name and their age. Print out a message
addressed to them that tells them the year that they will turn 100 years old.
Extras:

Add on to the previous program by asking the user for another number and printing
out that many copies of the previous message.

Print out that many copies of the previous message on separate lines. """

class problem_one:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def findBirthday(self):
        self.difference = 100 - self.age
        self.Birthday = 2018 + self.difference
        print('You will turn 100 on', self.Birthday)
    def printing(self, num_reps):
        self.num_reps = num_reps
        print('\nStarting to repeat:')
        for i in range(num_reps):
            problem_one.findBirthday(self)
    def printNewLines(self):
        for j in range(self.num_reps):
            print('\n')
            problem_one.findBirthday(self)

person_One = problem_one('P_one',23)
person_One.findBirthday()
person_One.printing(3)
person_One.printNewLines()




