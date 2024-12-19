from animale import Animale

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
