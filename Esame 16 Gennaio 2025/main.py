import pickle
import argparse
from utenti import *

utenti = list()

def seleziona_utente():
    if utenti == []:
        print("Nessun utente presente")
    else:
        c = 1
        for u in utenti:
            print(f"{c}. {u.getNome()}")
            c += 1
        i = int(input("\nScelta: "))-1
        menu_utente(utenti[i])

def crea_utente():
    nome = input("Inserisci il nome del nuovo utente: ")
    utenti.append(Utente(nome))
    print("Utente creato")

def uscita():
    quit()

def backup():
    with open("backup.dat", "wb") as f:
        pickle.dump(utenti, f)
    print("Backup esceguito con successo")

def get_backup():
    with open("backup.dat", "rb") as f:
        global utenti
        utenti = pickle.load(f)
    print("Backup caricato con successo")

def menu_utente(u):
    m_utente = [u.visualizzaPlaylist, u.inserisciBrano, u.visualizzaBrani, u.creaPlaylist, u.filtraggioBrani, u.esportaPlaylist]
    while True:
        i = int(input(f"\nCiao {u.getNome()}:\n"
                  "1. Visualizza le tue playlists\n"
                  "2. Inserire un nuovo brano in una playlist\n"
                  "3. Visualizza i brani di una playlist\n"
                  "4. Crea una nuova playlist\n"
                  "5. Filtrare tutti i tuoi brani per genere\n"
                  "6. Esportare una tua Playlist in un file\n"
                  "7. Torna al menu principale\n"
                  "\nScelta: ")) - 1
        if i == 6:
            return 0
        else:
            m_utente[i]()

def main():
    parser = argparse.ArgumentParser(description="Programma per gestire le playlist di un utente")
    parser.add_argument('nome', type=str, nargs='?', help="Il nome dell'utente")
    parser.add_argument('genere', type=str, nargs='?', help="Il genere dei brani da esportare")
    parser.add_argument('file', type=str, nargs='?', help="Il nome del file di output")

    args = parser.parse_args()

    if args.nome is None or args.file is None:
        menu = [seleziona_utente, crea_utente, backup, get_backup, uscita]
        while True:
            try:
                menu[int(input("\nMENU PRINCIPALE:\n"
                               "1. Seleziona utente\n"
                               "2. Crea utente\n"
                               "3. Backup\n"
                               "4. Ripristino backup\n"
                               "5. Uscita\n"
                               "\nScelta: "))-1]()
            except Exception as e:
                print("Scelta non valida: ")
    else:
        with open("backup.dat", "rb") as f:
            global utenti
            utenti = pickle.load(f)
        for u in utenti:
            if u.getNome() == args.nome:
                brani = u.filtraggioBrani_backgraund(args.genere)
                with open(args.file, "a") as f:
                    f.write(f"I tuoi BRANI di genere {args.genere}\n")
                    for b in brani:
                        if b.getGenere() == args.genere:
                            f.write(f"{b.getTitolo()} - {b.getArtista()} - {b.getGenere()} - {b.getDurata()} min\n")
                return 0
            else:
                print("Utente non presente nel sistema")



if __name__ == "__main__":
    main()