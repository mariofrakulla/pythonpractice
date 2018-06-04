""" Class Fraction """
class Fraction(object):
    """
    A number represented as a fraction
    """
    def __init__(self,num,denom):
        """ Num and denom are integers """
        assert type(num) == int and type(denom)== int
        self.num = num
        self.denom = denom
    def __str__(self):
        """ Returns a string representation of the fraction """
        return str(self.num) + '/' + str(self.denom)
    def __add__(self,other):
        """ Returns a new fraction representing the sum of the two fractions """
        top = self.num *other.denom + self.denom*other.num
        bottom = self.denom*other.denom
        return Fraction(top,bottom)
    def __sub__(self, other):
        """ Returns a new fraction representing the difference of the two fractions """
        top = self.num* other.denom - self.denom*other.num
        bottom = self.denom * other.denom
        return Fraction(top,bottom)
    def __float__(self):
        """ Returns a float value of the fraction """
        return self.num/self.denom
    def inverse(self):
        """ Returns the inverse of a fraction """
        return Fraction(self.denom,self.num)
a = Fraction(1,3)
b = Fraction(1,7)
c = a + b
print(a)
print(b)
print(c)
print(c.inverse())
