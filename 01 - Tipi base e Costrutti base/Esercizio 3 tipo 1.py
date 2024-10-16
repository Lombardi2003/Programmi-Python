# Scrivere un programma che prenda un valore inserito dall'utente
#   - Se è 1 stampa 'red'
#   - Se è 2 stampa 'blue'
#   - Se è 3 stampa 'green'
# Negli altri casi stampa un messaggio di errore

a = input('Inserisci: ')
if a=='1' :
    print('red')
elif a=='2' :
    print('blue')
elif a=='3' :
    print('green')
else :
    print('Errore!!!')
