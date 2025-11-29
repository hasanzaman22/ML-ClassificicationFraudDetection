import math

class Rational:
    def __init__(self,suret,mexrec):
        if mexrec == 0:
            raise ZeroDivisionError('0a bolmek olmaz') #raise - error kimi yox xeberdarliq kimi netice verir sifira bolende
        gcd = math.gcd(suret,mexrec)
        self.suret=suret // gcd
        self.mexrec = mexrec // gcd

    def __add__(self,kesr2): #__ dunder ve ya magic adlanir
        suret2 = self.suret * kesr2.mexrec + kesr2.suret*self.mexrec
        mexrec2 = self.mexrec * kesr2.mexrec
        return Rational(suret2,mexrec2)
    
    def __sub__(self,kesr2):
        suret2 = self.suret * kesr2.mexrec - kesr2.suret*self.mexrec
        mexrec2 = self.mexrec * kesr2.mexrec
        return Rational(suret2,mexrec2)

    def __mul__(self,kesr2):
        suret2 = self.suret * kesr2.suret
        mexrec2 = self.mexrec * kesr2.mexrec
        return Rational(suret2,mexrec2)
    
    def __truediv__(self,kesr2):
        suret2 = self.suret * kesr2.mexrec
        mexrec2 = self.mexrec * kesr2.suret
        return Rational(suret2,mexrec2)
    
    def __repr__(self):
        if self.mexrec == 1:
            return f'{self.suret}'
        else:
            return f'{self.suret} / {self.mexrec}'
    

a = Rational(8,7)
b = Rational(20,7)

print(a+b)































