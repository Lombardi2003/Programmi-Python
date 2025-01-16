from progetto import *

class Utente:

    def __init__(self,nome):
        self.progetti = list()
        self.nome = nome
    
    def get_nome(self):
        return self.nome
    
    def stampa_progetto(self):
        if self.progetti == []:
            print("Nessun Progetto")
        else:
            c = 1
            print("Elenco dei progetti")
            for i in self.progetti:
                print(f'{c}. {i.get_nome()}')
            s = int(input("\nScelta: ")) - 1

    def inserisci_progetto(self):
        nome = input("\nInserisci il nome del nuovo progetto: ")
        data_inizio = input("\nInserisci la data d'inizio: ")
        data_fine = input("\nInserisci la data di fine: ")
        self.progetti.append(Progetto(nome,data_inizio,data_fine))
        print("Progetto Creato!!")