import itertools
 
def nx(x, n):
    return list(itertools.combinations(x, n))

x={1,2,3,'A','B','C'}
n = 2

 
print(nx(x, n))
def mx(x, m):
    return list(itertools.combinations(x, m))

x={1,2,3,'A','B','C'}
m = 3

 
print(mx(x, m))
def lx(x, n):
    return list(itertools.combinations(x, l))

x={1,2,3,'A','B','C'}
l = 4

 
print(lx(x, l))
def lx(x, k):
    return list(itertools.combinations(x, k))

x={1,2,3,'A','B','C'}
k = 5

 
print(lx(x, k))
def jx(x, j):
    return list(itertools.combinations(x, j))

x={1,2,3,'A','B','C'}
j = 6

 
print(jx(x, j))
