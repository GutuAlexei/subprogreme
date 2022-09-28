import math
a = int(input('a= '))
b = int(input('b= '))
c = int(input('c= '))
d = int(input('d= '))
def perimetruaria(x,y,z):
    P=x+y+z
    sp = P/2
    A = math.sqrt(sp*(sp-x)*(sp-y)*(sp-z))
    return print('Perimetru = ', P, 'Aria = ', A)
if ((a > 0) and (b > 0) and (c > 0) and (d > 0)):
    if ((a+b>c) and (b+c>a) and (a+c>b)):
        print('Date pentru triunghiul abc')
        perimetruaria(a,b,c)
    else:
        print('triunghiul ABC nu exista')
    if ((a+b>d) and (b+d>a) and (a+d>b)):
        print('Date pentru triunghiul abd')
        perimetruaria(a,b,d)
    else:
        print('triunghiul ABD nu exista')
    if ((c+b>d) and (b+d>c) and (c+d>b)):
        print('Date pentru triunghiul bcd')
        perimetruaria(b,c,d)
    else:
        print('triunghiul BCD nu exista')
    if ((c+a>d) and (a+d>c) and (c+d>a)):
        print('Date pentru triunghiul acd')
        perimetruaria(a,c,d)
    else:
        print('triunghiul ACD nu exista')
else:
    print('nu sunt numere naturale')