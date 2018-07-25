""" Odd Or Even
Ask the user for a number. Depending on whether the number is even or odd, print out an appropriate message to the user.
Extras:
If the number is a multiple of 4, print out a different message.
Ask the user for two numbers: one number to check (call it num) and one number to divide by (check).
If check divides evenly into num, tell that to the user. If not, print a different appropriate message."""

class p_two:
    def __init__(self, num):
        self.num = num
    def Check(self):

        if self.num % 4 == 0:
            print('The number is even and divisible by 4.')
        elif self.num % 2 == 0:
            print('The number is even.')
        else:
            print('The number is odd.')
    def Give_and_Check(self, check, num):
        self.check = check
        self.num = num
        if self.num % self.check == 0:
            print(self.check ,'divides evenly into', self.num)
        else:
            print(self.check,'does not divide evenly into', self.num)


number_one = p_two(4)
number_one.Check()
number_one.Give_and_Check(5,6)

