import random
k=[]
s=0
n=int(input('n='))
for i in range (n):
    k.extend([random.randint(1, 100)])
print(k)
for i in k:
    if i<max(k):
        s+=1
print(s)

