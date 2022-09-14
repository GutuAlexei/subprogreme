n=int(input('Cate elemente are lista='))

def listint(nr):
    
    lista=[]
    for i in range(nr):
        try:
            ele=int(input('Elemntul'+ str(i+1) +' este=',))
        except ValueError:
            raise Error('Nu ati introdus corect, incercati din nou;)')
        lista.append(ele)
    return print(lista)
    
listint(n)


def listfloat(nr):
    
    lista=[]
    for i in range(nr):
        try:
            ele=float(input('Elemntul'+ str(i+1) +' este=',))
        except ValueError:
            raise Error('Nu ati introdus corect, incercati din nou;)')
        lista.append(ele)
    return print(lista)
    
listfloat(n)