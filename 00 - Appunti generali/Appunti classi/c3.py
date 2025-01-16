class MiaClass:

    attributo_1 = 10
    instanza = None
    #creatore - definizione della new, metodo in creazione di un oggetto non di inizializzazione
    def __new__(cls, *args, **kwargs):
        if MiaClass.instanza is None:
            MiaClass.instanza = super().__new__(cls) # stessa cosa di object.__new__(cls)
            return MiaClass.instanza
        else :
            return MiaClass.instanza
    #costruttore                # si chiama init il costruttore, avere due underscore avanti e indietro python prenderà quel metodono come tra i principali dell'interprete
    def __init__(self):
       pass

oggetto = MiaClass()
oggetto1 = MiaClass()
oggetto2 = MiaClass()
print(oggetto is oggetto1)