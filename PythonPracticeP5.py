""" Random Password Generator """
import string
import random

class Password:

    def GeneratePassword(self, size):
        self.list_to_Choose = string.ascii_letters + string.digits + string.punctuation
        self.size = size
        self.password = ""
        for i in range(self.size):
            self.password = self.password + (random.choice(self.list_to_Choose))


        return self.password

pass_one = Password()
print(pass_one.GeneratePassword(12))
