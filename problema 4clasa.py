import random 
a=random.randint(1,6)
b=random.randint(1,6)
s=1
while a!=b:
    a=random.randint(1,6)
    b=random.randint(1,6)
    if a!=b:
        print('1 zar=', a , '2 zar=', b)
    else:
        s=4*a
        print('1 zar=', a , '2 zar=', b, 'Suma de puncte', s)