import math
a = int(input('a= '))
b = int(input('b= '))
c = int(input('c= '))
def triunghi(z,x,y):
    if z<x+y and x<z+y and y<z+x:
        ma=0,5*math.sqrt(2*x**2+2*c**2-a**2)
        return print('MEdiana =', ma)
    else:
        print('Acestea marimi nu pot fi laturile triughiului')    
print(triunghi(a, b, c))