class A:
    def m1(self):
        print('hi')

class B:
    def m1(self):
        print('ho')
    
class C(A,B):
    i = 0
    def __init__(self):
        self.__a=0

c = C()
print(C.mro())    # ritornare in sola lettura l'ordine dei metodi di risoluzione
                    # così si può ritornare una 
                 # fino a quando non trova a classe proprio superiore
print(C.__bases__)# per elencare l'ordine di importanza delle classi
# Si può anche cambiare
C.__bases__= (B,A)
print(C.__bases__)
#funzione per verificare che un istanza fa parte di quell'oggetto o di un suo sottotipo
print(isinstance(c, C))
#funzione per verificare una classe se è un sottotipo di un altra classe
print(issubclass(C, A))
print(issubclass(A,C))
print()
print(c.__dict__)

print(c.i)
c.i=10
# così si va a modificare il dict
print(c.i)
print(C.i)