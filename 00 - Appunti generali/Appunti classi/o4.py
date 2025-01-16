# classi astratte con un decoratore e una libreria 
from abc import ABC, abstractmethod
# per far diventare una classe astratta bisogna inserire la libreria e con il decoratore di possono inserire i metodi astratti

class Astratta(ABC):
    @abstractmethod
    def metodo_astratto(self):
        pass

#oggetto_astratto = Astratta()
#print(oggetto_astratto)

# non funziona perchè abbiamo cercato di istanziare un oggetto astratto che non è isstanziabile

class Concreta(Astratta):
    def metodo_astratto(self):
        print('hi')

oggetto_concreto = Concreta()
print(oggetto_concreto)
oggetto_concreto.metodo_astratto()













class Concreta1(Astratta):
    def metodo_astratto(self):
        print('hi')
        
class Concreta2(Astratta):
    def metodo_astratto(self):
        print('hi!!!')


#ogg_concre_1 # fine appunti