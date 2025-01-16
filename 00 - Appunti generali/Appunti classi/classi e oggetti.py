class MiaClass:
    #definizione attributi
    attributo_classe_1 = 10
    attributo_classe_2 = 'stringa'  # Attributo legato alla classe

    #costruttore                # si chiama init il costruttore, avere due underscore avanti e indietro python prenderà quel metodono come tra i principali dell'interprete
    def __init__(self,c):
        self.c = c              # quando si vuole aggiungere un attributo di instanza si fa nella init

    #definizione metodi
    def metodo1(self,a,b):          # convezione si chiama self
        return a+b

#stampa attributi di classe
print(MiaClass.attributo_classe_1)
print(MiaClass.attributo_classe_2)

#istanziare un nuovo oggetto
oggetto1 = MiaClass()
print(oggetto1)
#stampa dell'attributo di un oggetto
print(oggetto1.attributo_classe_1)

#cambiando l'attributo di uno non cambia anche l'altro
oggetto2 = MiaClass()
oggetto2.attributo_classe_1 = 12
print(oggetto1.attributo_classe_1)

#chiamata del metodo
oggetto1.metodo1(1,2)