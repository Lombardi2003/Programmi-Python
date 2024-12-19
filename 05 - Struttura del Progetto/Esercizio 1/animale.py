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
        print("Sto camminando!!!")

    @abstractmethod
    def corre(self):
        print("Sto correndo!!!")