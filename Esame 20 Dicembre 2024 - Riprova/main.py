from utenti import Utente
import argparse
import pickle

utenti = list()

def uscita():
    quit()

def crea_utente():
    nome = input("Inserisci il nome dell'utente: ")
    utenti.append(Utente(nome))

def seleziona_utente():
    if utenti == []:
        print("Nessun Utente da selezionare")
    else:
        c = 1
        for i in utenti:
            print(f'{c}. {i.get_nome()}')

def menu_principale():
    return int(input("\nMENU PRINCIPALE:\n"
                     "1) Seleziona Utente\n"
                     "2) Crea Utente\n"
                     "3) Esci dal programma\n"
                     "\nScelta: "))-1
def main():
    menu = [seleziona_utente, crea_utente, uscita]

    while True:
        try:
            menu[menu_principale()]()
        except Exception:
            print("Errore!!!")

if __name__ == '__main__':
    main()