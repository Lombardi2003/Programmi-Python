# Trattare l’attributo “malato” come descrittore (che considera anche l’attributo “spavaldo”).

from abc import ABC, abstractmethod

class Animale(ABC):
    zampe = 4
    coda = True
    eta = 0
    sesso = None

    def __init__(self, zampe, coda, eta, sesso):
        self.zampe = zampe
        self.coda = coda
        self.eta = eta
        self.sesso = sesso

    @abstractmethod
    def cammina(self):
        pass

    @abstractmethod
    def corre(self):
        pass

class MalatoDescrittore:
    def __get__(self, instance, owner):
        if instance is None:
            return self
        if instance.__spavaldo:
            return False
        return instance.__malato

    def __set__(self, instance, value):
        instance.__malato = value

class Cane(Animale):

    count=0

    # Due under score significa attributo privato
    __malato = MalatoDescrittore()
    __spavaldo = False

    def __new__(cls, *args, **kwargs):
        cls.count += 1
        return super().__new__(cls)  # Il super serve per la corretta creazione dell'oggetto

    def __init__(self, zampe, coda, eta, sesso):
        Animale.__init__(self, zampe, coda, eta, sesso)
        self.__malato = False

    def cammina(self):
        print("Sto camminando!!!")

    def corre(self):
        print("Sto correndo!!!")

    def istanze():
        return Cane.count

    def abbaia(self):
        print("Ufff!!!")

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

class Gatto(Animale):
    count = 0

    __malato = False
    __spavaldo = False

    def __init__(self, zampe, coda, eta, sesso):
        Animale.__init__(self, zampe, coda, eta, sesso)

    def cammina(self):
        print("Sto camminando!!!")

    def corre(self):
        print("Sto correndo!!!")

    def Miagola(self):
        print("Miao!!!")

    def istanze():
        return Gatto.count

# Creazione di istanze per testare la classe Cane
cane1 = Cane(4, True, 2, 'Maschio')
cane2 = Cane(4, True, 3, 'Femmina')
print(f'Il numero di istanze create della classe Cane è {Cane.istanze()}')

if cane1.malato:
    print('Il cane è malato')
else:
    print('Il cane non è malato')

cane1.abbaia()
cane1.malato = True

if cane1.malato:
    print('Il cane è malato')
else:
    print('Il cane non è malato')

# Test dell'operatore + per la classe Cane
cucciolo = cane1 + cane2
print(f"Il cucciolo è un {cucciolo.sesso}")

# Creazione di istanze per testare la classe Gatto
gatto1 = Gatto(4, 1, 20,'Femmina')
gatto2 = Gatto(4, 2, 21,'Maschio')
print(f'Il numero di istanze create della classe Gatto è {Gatto.istanze()}')

gatto1.Miagola()