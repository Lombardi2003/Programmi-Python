# Scrivere una classe Cane che definisca i seguenti attributi:
#   - zampe (default 4)
#   - coda (default True)
#   - età (default=0)
#   - sesso
# E i seguenti metodi
#   - abbaia
#   - cammina
#   - corri
#
# Aggiungere un attributo di classe che conti il numero di volte che è stata istanziata la classe stessa.
#
# Aggiungere un metodo chiamabile direttamente sulla classe che riporti tale numero
#
# Aggiungere due attributi privati a Cane:
#   - malato (default False)
#    - spavaldo (default False)
#
# Aggiungere dei getters e setters per accederli e modificarli (nel modo classico)

class Cane:
    zampe = 4
    coda = True
    eta = 0
    sesso = None

    count = 0

    # Due under score significa attributo privato
    __malato = False
    __spavaldo = False

    def abbaia(self):
        print("Ufff!!!")

    def cammina(self):
        print("Sto camminando!!!")

    def corre(self):
        print("Sto correndo!!!")

    def __new__(cls, *args, **kwargs):
        cls.count += 1
        return super().__new__(cls)                 # il super serve per la corretta creazione dell'oggetto

    def __init__(self, zampe, coda, eta, sesso):
        self.zampe = zampe
        self.coda = coda
        self.eta = eta
        self.sesso = sesso


    def istanze():
        return Cane.count
    
    # setters
    def set_malato(self, malato):
        self.__malato = malato

    def get_spavaldo(self, spavaldo):
        self.__spavaldo = spavaldo

    # getters
    def get_malato(self):
        return self.__malato
    
    def get_spavaldo(self):
        return self.__spavaldo

c0 = Cane(4, True, 2, 'Maschio')
c1 = Cane(3, False, 5, 'Femmina')
c2 = Cane(4, True, 10, 'Maschio')
c3 = Cane(4, True, 3, 'Femmina')
c4 = Cane(3, False, 6, 'Maschio')
print(f'Il numero di istanze create della classe Cane è {Cane.istanze()} \n')

c = Cane(4, True, 7, 'Maschio')

if c.get_malato() is True :
    print('Il cane è malato')
else:
    print('Il cane non è malato')

c.abbaia()
c.set_malato(True)

if c.get_malato() is True :
    print('Il cane è malato')
else:
    print('Il cane non è malato')