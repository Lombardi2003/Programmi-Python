class MiaClass:

    attributo_1 = 10
    instanza = None
    #costruttore                # si chiama init il costruttore, avere due underscore avanti e indietro python prenderà quel metodono come tra i principali dell'interprete
    def __init__(self,c):
        self.c = c              # quando si vuole aggiungere un attributo di instanza si fa nella init

    #definizione metodi
    def metodo1(self,a,b):          # convezione si chiama self
        return self.c+a+b

    #creatore - definizione della new, metodo in creazione di un oggetto non di inizializzazione
    def __new__(cls, *args, **kwargs):
        if MiaClass.instanza is None:
            MiaClass.super().__new__(cls)# stessa cosa di object.__new__(cls)
            return MiaClass.instanza
        else :
            return MiaClass.instanza

    #metodo statico
    @staticmethod
    def metodo_statico():
        print(f'Metodo statico: {MiaClass.attributo_1}')
    
    #metodo di classe -> quando si chiama è proprio la classe stessa
    @classmethod
    def metodo_classe(cls):
        pass
    
oggetto = MiaClass(10)
print(oggetto.__dict__)
oggetto1 = MiaClass(10)
oggetto1.d=20                   # inserire  una componente in più
print(oggetto.__dict__)
print(oggetto1.__dict__)
#chiamata al metodo
print(oggetto.metodo1(1,2))

MiaClass.metodo_statico()

intClass = int
print(intClass)