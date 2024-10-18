# Scrivere un programma che chieda all'utente di immettere una serie di valori terminata dal simbolo '#'
#
# Dopodichè applica una funzione a vostro piacere su tutti gli elementi
#
# Non usare un ciclo per l'applicazione della funzione

lista = []
while True: 
    i = input('Inserisci un numero oppure # per terminare il programma: ')
    if i == '#':
        break
    else:
        lista.append(int(i))
print('La lista è: ',lista)

def f(i):
    print(i*2)
#
#for i in l:
#    print(f(i))
# Oppure
list(map(f,lista))