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
#
# Modificare i getters e setters usando @property
#
# Bis: Definire un comportamento speciale per l’attributo malato: 
#      ritorno il valore di malato MA se spavaldo è True ritorna sempre False
#
# Definire un comportamento per l'operatore + tra due Cane. Per esempio, nasce un cucciolo.
# Prevedere comportamenti diversi in base agli attributi età e sesso dei Cane coinvolti.
#
# - Se entrambi i cani sono maschi o entrambi sono femmine, non può nascere un cucciolo.
# - Se uno dei cani è maschio e l'altro è femmina, può nascere un cucciolo. Le caratteristiche del 
#   cucciolo (come età e sesso) possono essere definite in base alle caratteristiche dei genitori.
# 
# Doc: https://docs.python.org/3/reference/datamodel.html#object.__add__

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
    
    # Getter e setter per malato
    @property
    def malato(self):
        if self.__spavaldo: 
            return False 
        return self.__malato
    @malato.setter
    def malato(self, malato):
        self.__malato = malato

    # Getter e setter per spavaldo
    @property
    def spavaldo(self):
        return self.__spavaldo
    @spavaldo.setter
    def spavaldo(self, spavaldo):
        self.__spavaldo = spavaldo

     # Definizione del comportamento per l'operatore +
    def __add__(self, altro):
        if not isinstance(altro, Cane):
            raise TypeError("Entrambi gli oggetti devono essere di tipo Cane")

        if self.sesso == altro.sesso:
            print("Non può nascere un cucciolo da due cani dello stesso sesso")
            return 0

        # Creazione del cucciolo
        cucciolo = Cane(zampe=4, coda=True, eta=0, sesso="Maschio" if self.sesso == "Femmina" else "Femmina")
        print(f"È nato un cucciolo da {self.sesso} e {altro.sesso}")

        return cucciolo   

c0 = Cane(4, True, 2, 'Maschio')
c1 = Cane(3, False, 5, 'Femmina')
c2 = Cane(4, True, 10, 'Maschio')
c3 = Cane(4, True, 3, 'Femmina')
c4 = Cane(3, False, 6, 'Maschio')
print(f'Il numero di istanze create della classe Cane è {Cane.istanze()} \n')

c = Cane(4, True, 7, 'Maschio')

if c.malato is True :
    print('Il cane è malato')
else:
    print('Il cane non è malato')

c.abbaia()
c.malato = True

if c.malato is True :
    print('Il cane è malato')
else:
    print('Il cane non è malato')

cucciolo = c1 + c2      #Output:È nato un cucciolo da Maschio e Femmina print(cucciolo.sesso) # Output: Femmina