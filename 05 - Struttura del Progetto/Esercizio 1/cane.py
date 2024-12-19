from animale import Animale

class Cane(Animale):

    count=0

    # Due under score significa attributo privato
    __malato = False
    __spavaldo = False

    def __new__(cls, *args, **kwargs):
        cls.count += 1
        return super().__new__(cls)  # Il super serve per la corretta creazione dell'oggetto

    def __init__(self, zampe, coda, eta, sesso):
        Animale.__init__(self, zampe, coda, eta, sesso)

    def cammina(self):
        print("Sto camminando!!!")

    def corre(self):
        print("Sto correndo!!!")

    def istanze():
        return Cane.count

    def abbaia(self):
        print("Ufff!!!")

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