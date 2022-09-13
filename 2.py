m=int(input('m='))
n=int(input('n='))

def f(sa):
    p=1
    s=0
    for i in range(1, sa+1):
        p*=1
    return p

fac= f(m) * (f(n-m))    

c=f(n)/ fac

print(c)



