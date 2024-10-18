# Scrivere un programma che chieda all'utente di immettere una serie di valori terminata dal simbolo '#'
#
# Dopodichè applica una funzione a vostro piacere su tutti gli elementi
#
# Non usare un ciclo per l'applicazione della funzione
#
# Modificare il programma precedente in modo che l’utente possa inserire solo numeri.

lista = []
while True: 
    i = input('Inserisci un numero oppure # per terminare il programma: ')
    try :
        if i == '#':
            break
        else:
            lista.append(int(i))
    except Exception:
        print('Non hai inserito un numero')

print('La lista è: ',lista)
print('Stampa dei valori raddoppiati:')
def f(i):
    print(i*2)
list(map(f,lista))