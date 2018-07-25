""" Polymorphism example
Definition: Polymorphism allows a method with the same name in different classes to perform
different tasks."""

class book:
    def __init__(self, x):
        self.price = x

class stockist(book):
    def __init__(self, x):
        book.__init__(self, x)
    def commission(self):
        self.comm = 0.05*self.price
        print('Commission of the stockist is: ', self.comm)
class distributor(book):
    def __init__(self,x):
        book.__init__(self, x)
    def commission(self):
        self.comm = 0.07*self.price
        print('Commission of the distributor is: ', self.comm)

class retailer(book):
    def __init__(self, x):
        book.__init__(self,x)
    def commission(self):
        self.comm = 0.1*self.price
        print('Commission of the retailer is: ', self.comm)
inst_one = distributor(100)
inst_one.commission()
inst_two = stockist(100)
inst_two.commission()
inst_three = retailer(100)
inst_three.commission()
