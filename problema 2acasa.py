import random
k=[]
n=1 
for i in range (10):
    for i in range (5):
        k.extend([random.randint(1, 36)])
    print('Rezultatul', n , 'Superlato din 5 numere', k)
    k=[]
    n+=1