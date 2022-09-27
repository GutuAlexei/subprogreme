from calendar import c
import math
from symbol import compound_stmt


a=int(input('a='))
b=int(input('b='))
d=int(input('c='))
def divizor(z,x,y):
    l1=[]
    for i in range (1, int(max(z,x,y)/2)+1):
        if x% i ==0 and z %i ==0:
            l1.append(i)
        return l1

print("a) un divizor comun:", divizor(a,b,d))

def multiplu(z,x,y):
    mz=[]
    mx=[]
    my=[]
    tot=[]

    for i in range (1, max(z,x,y)):
        mz.append(z*i)
        mx.append(x*i)
        my.append(y*i)
    
    for i in mz:
        if i in mx and i in my:
            tot.append(i)

    return tot[0:1]

print("b) un multiplu comun:",multiplu(a,b,d))

def minim(z,x,y):
    if z>y and x>y:
        return y
    if z>x and y>x:
        return x
    if y>z and x>z:
        return z
    else:
        return print('x si y sunt la fel')

print("c)Minim:",minim(a,b,d))

def maxim(z,x,y):
    if z<y and x<y:
        return y
    if z<x and y<x:
        return x
    if y<z and x<z:
        return z
    else:
        return print('x si y sunt la fel')

print("d)Maxim:",maxim(a,b,d))

def treimultiplu(z,x,y):
    mz=[]
    mx=[]
    my=[]
    tot=[]

    for i in range (1, max(z,x,y)):
        mz.append(z*i)
        mx.append(x*i)
        my.append(y*i)
    
    for i in mz:
        if i in mx and i in my:
            tot.append(i)

    return tot[0:3]

print("e)3 multipli comuni:",treimultiplu(a,b,d))

def triunghi(z,x,y):
    if z<x+y and x<z+y and y<z+x:
        semisuma = (z+x+y)/2
        Aria = math.sqrt(semisuma*(semisuma-z)*(semisuma-x)*(semisuma-y))
        return print('g)Aria este:', Aria, 'Perimetru este ', int(semisuma*2))
    else:
        print('Acestea marimi nu pot fi laturile triughiului')    
print(triunghi(a, b, d))



def ecuatia(z,q,y):

    delta=q**2-4*z*y
    x1=(-q-math.sqrt(delta))/z
    x2=(-q+math.sqrt(delta))/z
    xx=-q/2*z
    if delta > 0 :
        return print('h)x1=',x1,'x2=' ,x2)
    if delta ==0 :
        return print('h)x=', xx)
    if delta < 0 :
        return print('h)Solutie vida')

print(ecuatia(a, b, d))

