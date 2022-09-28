import math
a = int(input('a= '))
b = int(input('b= '))
c = int(input('c= '))
def triunghi(z,x,y):
    if z<x+y and x<z+y and y<z+x:
        semisuma = (z+x+y)/2
        Aria = math.sqrt(semisuma*(semisuma-z)*(semisuma-x)*(semisuma-y))
        ha=(2*Aria)/(z)
        return print('Inaltimea este', ha )
    else:
        print('Acestea marimi nu pot fi laturile triughiului')    
print(triunghi(a, b, c))