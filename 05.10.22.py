import random 
n=int(input("Nr de cifre ="))
s=0
s1=0
for i in range(n):
    i=random.randint(-50, 50)
    print(i)
    if i<0:
        s+=i
    if i>0:
        s1+=i
print('Suma numerilor pozitive=', s1)
print('Suma numerilor negative=',s)

    
