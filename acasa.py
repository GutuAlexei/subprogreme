import math
from re import M, S
m=int(input('m='))
n=int(input('n='))

def suma():
    return m+n
print('a)Suma=' , suma())

def produs():
    return m*n
print('b)produs=' ,produs())

def media():
    return (m+n)/2
print('c)Media aritmetica=' ,media())

def divizor(m,n):
    while m!=n:
        if m>n: m = m - n
        else: n = n - m
    return n
print('d)CEl mai mic divizor comun =', divizor(m,n))
print('e)CEl mai mare divizor comun =', str(m*n// divizor(m,n)))

def minim(m,n):
    return min(m,n)
print('f)Minim=', minim(m,n))

def maxim(m,n):
    return max(m,n)
print('g)Maximum=',maxim(m,n))

def sumafor():
    c=0
    a=int(input('a= '))
    b=int(input('b= '))
    c= a+b
    return c
print('h)a', '+', 'b', '=', sumafor())

def produsfor():
    c=0
    a=int(input('a= '))
    b=int(input('b= '))
    c= a*b
    return c
print('i)a', '*', 'b', '=', produsfor())

def divizorcomun(m,n):
    divisor = 0
    print("j)Divizor comuni ",m," si ",n," sunt -")
    for i in range(1,min(m,n)+1):
        if m%i == n%i == 0:
            divisor = i
            print(divisor)
    return i
print(divizorcomun(m,n))

def multiplicomuni(m,n):
    l1=[]
    for i in range(1,m**5):
        for j in range(1,n**5):
            if m*i==n*j:
                l1.append(m*i)
            if len(l1)==5:
                return l1
print('k)5 Multipli comuni=',multiplicomuni(m,n))

def cifrecomune(m,n):
    l2=[]
    for i in [z for z in str(m)]:
        for j in [q for q in str(n)]:
            if i==j:
                l2.append(int(i))
    return l2
print('l)Cifre comune in ambele=',cifrecomune(m,n))

def cifrec(m,n):
    l3=[]
    l4=[]
    for i in str(n):
        l4.append(i)
    for j in str(m):
            if j not in l4 and j not in l3:
                l3.append(j)
    return l3
print ('m)Sunt in primul , dar nu in al 2lea=',cifrec(m,n))


