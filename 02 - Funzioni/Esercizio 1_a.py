# Scrivere un programma che chieda all'utente di immettere una serie di valori terminata dal simbolo '#'
#
# Dopodichè applica una funzione a vostro piacere su tutti gli elementi
#
# Non usare un ciclo per l'applicazione della funzione

def funzione():
    a = int(input("Inserisci un valore: "))
    if a!='#':
        stampa_per_2(a)
    else:
        print("Fine!!!\n")

def stampa_per_2(a):
    print(a*2)
    funzione()

funzione()