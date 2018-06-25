""" Operator overloading examples """

""" + __add__"""
""" == __eq__"""
class rectangle:
    def __init__(self, x, y):
        self.l = x
        self.b = y
    def __str__(self):
        return 'Side one is %d, Side two is %d'%(self.l, self.b)
    def __add__(self, other):
        return rectangle(self.l + other.l, self.b + other.b)
    def __eq__(self, other):
        return (self.l == other.l)and(self.b == other.b)
    def rectArea(self):
        self.area = self.b * self.l
        print('The area is: ', self.area)

m = rectangle(3,5)
n = rectangle(7,13)
m.rectArea()
n.rectArea()
d = m + n
d.rectArea()

if m == n:
    print('The rectangles m, n have equal areas')

else:
    print('The rectangles m, n do not have equal areas')




