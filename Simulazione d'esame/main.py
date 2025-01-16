from utente import *

utente = list()

def scelta_utenti():
    if utente == []:
        print("Nessun Utente")
    else:
        print("Elenco degli utenti")
        u = True
        c = 1
        for i in utente:
            print(f'{c}. {i.get_nome()}')
        s = int(input("\nScelta: ")) - 1
        f_utente = [i.stampa_progetto(), i.inserisci_progetto()]
        while u == True:
            u = menu_utente(s)
            if u == 3:
                return 0
            else:
                try:
                    f_utente[u-1]()
                except IndexError:
                    print("Scelta errata")

def crea_utente():
    nome = input("\nInserisci il nome del nuovo utente: ")
    u = Utente(nome)
    utente.append(u)
    print("Utente Creato!!")

def uscita():
    quit()

def menu_utente(s):
    return int(input(f"\nBenvenuto Utente {utente[s].get_nome()}:\n"
          "1) Aggiungi attività ad un Progetto\n"
          "2) Crea Progetto\n"
          "3) Torna al Menu Principale"
          "\nScelta: "))

def menu_principale():
    return int(input("\nMenu:\n"
          "1) Seleziona Utente\n"
          "2) Crea Utente\n"
          "3) Esci dal Programma"
          "\nScelta: "))

menu = [scelta_utenti,crea_utente,uscita]  
while True:
    try:
        menu[menu_principale()-1]()
    except IndexError:
        print("Scelta errata")