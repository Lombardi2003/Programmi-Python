class MiaClass:

    attributo_1 = 10
    attributo_2 = 'stringa'
    #costruttore                # si chiama init il costruttore, avere due underscore avanti e indietro python prenderà quel metodono come tra i principali dell'interprete
    def __init__(self):
       #variabile semi privata
       self._x = 10
       #variabile privata
       self.__y = 20
    
    def __setattr__(self, key, value):
        print('__setattr__')
        if key == 'z':
            super().__setattr__(key,value)

oggetto = MiaClass()
#accedo alla variabile privata
oggetto._x = 12

print(oggetto._x)
print(oggetto._MiaClass__y) # slide


# metodi con __

l = [1,2,3]
print(l[0])
print(l.__getitem__(0))

i = 10
j=12
print(i+j)
print(i.__add__(j))
print(str(i))
print(i.__str__())

l = [1,2,3]
l[0] = 8
# l.__setitem__(0) = 9  -> controllare

# setatr__ -> ce un errore nell'insieme
oggetto.z = 10