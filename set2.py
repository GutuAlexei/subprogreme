X={1,3,'a',4,'c','d',5,8,2,21}
Y={2,'a','c',8,4,9,'e',3}
reu=X.union(Y)
print('a)', reu)
inter=X.intersection(Y)
print('b)',inter)
xscady=X-Y
print('c)',xscady)
yscadx=Y-X
print('d)',xscady.union(yscadx))
print('e)',yscadx.intersection(xscady))