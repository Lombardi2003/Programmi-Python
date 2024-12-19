# Scrivere una classe Cane che definisca i seguenti attributi:
#   - zampe (default 4)
#   - coda (default True)
#   - età (default=0)
#   - sesso
# E i seguenti metodi
#   - abbaia
#   - cammina
#   - corri

class Cane:
    zampe = 4
    coda = True
    eta = 0
    sesso = None

    def abbaia():
        print("Abbaio!!!")

    def cammina():
        print("Cammino!!!")

    def corre():
        print("Corro!!!")

    def __init__(self, zampe, coda, eta, sesso):
        self.zampe = zampe
        self.coda = coda
        self.eta = eta
        self.sesso = sesso

c = Cane(4, True, 2, 'Maschio')
print(c)