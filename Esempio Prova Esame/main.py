from utenti import *
import pickle
utenti = list()
# Stringa delimiter per i menu
DELIM = "*-------------------------------------------------*\n"

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

# funzioni di utility
def stampa_utenti():
    if not utenti:
        print('Nessun utente inserito')
        return False
    else:
        for ind in range(len(utenti)):
            print(f'{ind + 1}. {utenti[ind]}')
        return True
def valida_int(titolo='Inserisci un numero: ', shift=True):
    if shift:
        sh = 1
    else:
        sh = 0
    try:
        scelta = int(input(titolo)) - sh
        if scelta < 0:
            raise IndexError
    except ValueError:
        raise ValueError('Inserisci un numero')
    except IndexError:
        raise IndexError('Scelta non valida')
    else:
        return scelta
def valida_str(titolo):
    try:
        inp = input(f'Inserisci {titolo}: ').strip()
        if not inp:
            raise ValueError
        return inp
    except ValueError:
        raise ValueError('Errore: campo non compilato')

# Menu oggetto
def menu_oggetto(user, obj, op):
    if op == 2:
        user.magazzino.rm_oggetto(obj)
    elif op == 3:
        user.magazzino.preleva_oggetto(obj)
    elif op == 4:
        user.magazzino.restituisci_oggetto(obj)
    elif op == 5:
        movimenti = user.magazzino.get_movimenti(obj)
        if not movimenti:
            print('Nessun movimento')
        else:
            for movimento in movimenti:
                print(f'{movimento}')
    elif op == 6:
        print(f'Quantità {obj}: {obj.quantita}')
    elif op == 7:
        user.magazzino.export_movimenti(obj, user.username)

# Menu utente
def menu_utente(user):
    while True:
        print(DELIM + f'Benvenuto, {user}\n' +
              '1. Inserisci oggetto in magazzino\n'
              '2. Elimina oggetto\n'
              '3. Preleva oggetto\n'
              '4. Restituisci oggetto\n'
              '5. Visualizza i movimenti di un oggetto\n'
              '6. Visualizza quantità disponibile\n'
              '7. Esporta movimenti di un oggetto\n'
              '8. Menu principale\n'
              )
        try:
            op_u = valida_int(shift=False)
            if op_u == 1:
                nome_obj = valida_str('il nome dell\'oggetto')
                qta = valida_int(titolo='Inserisci la quantità: ', shift=False)
                if qta <= 0:
                    raise ValueError('Inserisci almeno 1 oggetto')
                user.magazzino.add_oggetto(nome_obj, qta)
                print("Oggetto inserito correttamente")
            elif 2 <= op_u <= 7:
                user.magazzino.stampa_oggetti()
                obj_ind = valida_int(titolo='Inserisci l\'indice dell\'oggetto: ')
                obj_scelto = user.magazzino.oggetti[obj_ind]
                menu_oggetto(user, obj_scelto, op_u)
            elif op_u == 8:
                break
            if not 0 < op_u <= 8:
                raise IndexError('Operazione non permessa')
        except Exception as e:
            print(e)

# Sottomenu principali
def scegli_utente():
    while True:
        print(DELIM + 'Scegli utente')
        if not stampa_utenti():
            break
        try:
            ind_u = valida_int(titolo='Inserisci l\'indice dell\'utente: ')
            menu_utente(utenti[ind_u])
            break
        except Exception as e:
            print(e)
def crea_utente():
    while True:
        print(DELIM + 'Crea utente')
        try:
            username = valida_str('il nome utente')
            utenti.append(Utente(username))
            print(f'Utente {utenti[-1]} creato')
            break
        except Exception as e:
            print(e)
def esci():
    print(DELIM + 'Esco dal programma')
    quit()

MENU_OP = [scegli_utente, crea_utente, backup, get_backup, esci]
# Main menu loop
while True:
    print(DELIM + 'Menu principale\n'
          '1. Scegli utente\n'
          '2. Crea utente\n'
          '3. Fai il backup\n'
          '4. Ripristina il backup\n'
          '5. Esci\n')
    try:
        op = valida_int(DELIM + 'Inserisci l\'indice dell\'operazione: ')
        MENU_OP[op]()
    except Exception as e:
        print(e)