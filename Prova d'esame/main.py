from utente import Utente
import pickle
utenti = list()

# funzioni per il backup
def backup():
    with open('backup.dat', 'wb') as bkp:
        pickle.dump(utenti, bkp)
    print('Backup effettuato su \'backup.dat\'')
def get_backup():
    with open('backup.dat', 'rb') as bkp:
        global utenti
        utenti = pickle.load(bkp)
    print('Backup ripristinato da \'backup.dat\'')

def stampa_utente():
    if utenti == []:
        print("\nNessun Utente")
    else:
        print("\nStampa di tutti gli Utenti")
        c = 1
        for i in utenti:
            print(f'{c}. {i.get_nome()}')
            c+=1
        scelta = int(input("\nScelta: "))-1
        if utenti[scelta].get_ruolo() == 'Subordinato':
            menu_utente_sub(scelta)
        else:
            menu_utente_res(scelta)

def crea_utente():
    nome = input("Inserisci il nome dell'utente: ")
    try:
        stipendio = int(input("Inserisci lo stipendio orario: "))
    except ValueError:
        print("Errore!!!")
        return 0
    ruolo = input("Inserisci il ruolo dell'utente: ")
    if ruolo == 'Subordinato':
        responsabile = input("Inserisci anche il responsabile d questo utente: ")
        if utenti == []:
            print("Errore!!!")
            return 0
        else:
            for i in utenti:
                if i.get_nome() == responsabile:
                    u = Utente(nome,stipendio,ruolo,responsabile)
                    break
                print("Errore!!!")
                return 0
        
    elif ruolo == 'Responsabile':
        u = Utente(nome,stipendio,ruolo,'Nessuno')
    else:
        print("Errore!!!")
        return 0
    utenti.append(u)
    print(f"UTENTE {u.get_nome()} creato con successo")

def menu_utente_sub(u):
    while True:
        rich = [utenti[u].nuova_richiesta,utenti[u].vis_richieste,utenti[u].tot_denaro,utenti[u].esporta_richiesta]
        print(f"BENVENUTO {utenti[u].get_nome()}, sei {utenti[u].get_ruolo()}\n")
        s = int(input("1) Effettua richiesta\n"
                    "2) Visualizza richieste eseguite\n"
                    "3) Richiedere il coteggio delle ore accettate e del relativo importo in denaro\n"
                    "4) Selezionare una richiesta da esportare\n"
                    "5) Tornare al Menu principale\n"
                    "\nScelta: ")) - 1
        if s == 4:
            return 0
        else:
            rich[s]()
    

def menu_principale():
    return int(input("\nMENU PRINCIPALE\n"
                     "1) Scegli Utente\n"
                     "2) Crea Utente\n"
                     "3) Eseguire il Backup\n"
                     "4) Ripristinare il Backup\n"
                     "5) Esci dal programma\n"
                     "\nScelta: "))

def menu_utente_res(u):
    while True:
        nome = utenti[u].get_nome()
        print(f"BENVENUTO {utenti[u].get_nome()}, sei {utenti[u].get_ruolo()}\n"
            "Le richieste a tuo carico sono:")
        c = 1
        for i in utenti:
            if i.get_responsabile() == nome:
                rich = i.get_richieste()
                for j in rich:
                    if j.get_status() == 'In attesa':
                        print(f"{c}. Subordinato: {i.get_nome()} richiede {j.get_ore()*i.get_stipendio()}")
                        c+=1
                    else:
                        continue
                print("")
        s = int(input("\n\n1) Modificare una richiesta\n"
                  "2) Tornare al menu principale\n"
                  "\nScelta: "))
        if s == 2: 
            return 0
        else:
            n = input("Inserisca il nome del Subordinato: ")
            for i in utenti:
                c = 0
                if i.get_nome() == n:
                    print("Ha le seguenti richieste: ")
                    rich = i.get_richieste()
                    for j in rich:
                        print(f"{c}. Richiesta di {i.get_stipendio()*j.get_ore()}")
                        c+=1
                    scelta = int(input("Scegliere quale richiesta modificare: "))
                    i.rich[scelta].set_status(input("Accettato o Rifiutato???"))


def uscita():
    quit()

menu = [stampa_utente,crea_utente,backup,get_backup,uscita]

while True:
    try:
        menu[menu_principale()-1]()
    except IndexError:
        print("Errore!!!")
