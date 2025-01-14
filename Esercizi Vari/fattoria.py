class Fattoria:
    n_mucche_max = 10

    def __init__(self):
        n_mucche = 0
    
    @classmethod
    def mod_n_mucche_max(cls, n):
        cls.n_mucche_max = n
    
    @classmethod
    def stampa_n_mucche_max(cls):
        print("Il massimo è ", cls.n_mucche_max)

f1 = Fattoria()

f1.stampa_n_mucche_max()

f1.mod_n_mucche_max(15)

Fattoria.stampa_n_mucche_max()
