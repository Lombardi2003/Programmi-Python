import pickle

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

# funzione per esportare
def export_movimenti(self, obj, username):
    # Qui parte il salvataggio
    with open(f'{username}_{obj.nome}.txt', 'w') as exp:
        movimenti = self.get_movimenti(obj)
        for m in movimenti:
            exp.write(f'{m}\n')
    print(f'Movimenti di {obj} esportati')