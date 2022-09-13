a=int(input('a='))
b=int(input('b='))
c=int(input('c='))
d=int(input('d='))

from fractions import Fraction




def sfractii():
    s=Fraction(a,b)+Fraction(c,d)
    return s

def pfractii():
    p=Fraction(a,b)*Fraction(c,d)
    return p

print('suma=', sfractii(), 'produsul=',pfractii() )

