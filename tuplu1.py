e1=('Eugen', 'Python', 'M', 2, 6, 9)
e2=('Alexei', 'C++', '?F', 10, 8, 9)
e3=('Alexandru', 'Programistavici', 'M', 10, 9, 9)
s1=round(sum(e1[3:])/3,2)
s2=round(sum(e2[3:])/3,2)
s3=round(sum(e3[3:])/3,2)
print('a)Nota medie la 1 elev',s1)
print('a)Nota medie la 2 elev',s2)
print('a)Nota medie la 3 elev',s3)

if e1[3]<5 or e1[4]<5 or e1[5]<5:
    print('b)Rpetent:', e1[0], e1[1])
if e2[3]<5 or e2[4]<5 or e2[5]<5:
    print('b)Rpetent:',e2[0], e2[1])
if e3[3]<5 or e3[4]<5 or e3[5]<5:
    print('b)Rpetent:',e3[0], e3[1])
if e1[3]>5 and e1[4]>5 and e1[5]>5 and e2[3]>5 and e2[4]>5 and e2[5]>5 and e3[3]>5 and e3[4]>5 and e3[5]>5:
    print('b)Elevi repetenti nu sunt')
if e1[3]>8 and e1[4]>8 and e1[5]>8:
    print('c)Emenent:', e1[0], e1[1])
if e2[3]>8 and e2[4]>8 and e2[5]>8:
    print('c)Emenent:',e2[0], e2[1])
if e3[3]>8 and e3[4]>8 and e3[5]>8:
    print('c)Emenent:',e3[0], e3[1])
if e1[3]<8 and e1[4]<8 and e1[5]<8 and e2[3]<8 and e2[4]<8 and e2[5]<8 and e3[3]<8 and e3[4]<8 and e3[5]<8:
    print('c)Elevi emenenti nu sunt')